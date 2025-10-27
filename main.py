from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import instaloader
from datetime import datetime
import requests

app = FastAPI(title="Instagram API", description="API baraye dastresi be etelaat Instagram", version="1.0")



class ProfileRequest(BaseModel):
    username: str



class ReelRequest(BaseModel):
    link: str



L = instaloader.Instaloader(sleep=True, max_connection_attempts=3)



@app.post("/profile")
def get_profile_info(req: ProfileRequest):
    try:
        profile = instaloader.Profile.from_username(L.context, req.username)
        profile_status = "Private" if profile.is_private else "Public"
        return {
            "username": profile.username,
            "full_name": profile.full_name,
            "followers": profile.followers,
            "followees": profile.followees,
            "post_count": profile.mediacount,
            "biography": profile.biography,
            "profile_url": f"https://www.instagram.com/{profile.username}/",
            "status": profile_status
        }
    except instaloader.exceptions.ProfileNotExistsException:
        raise HTTPException(status_code=404, detail="Profile vojood nadarad")
    except instaloader.exceptions.LoginRequiredException:
        raise HTTPException(status_code=403, detail="Profile khosusi ast, login niaz ast")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/reel")
def get_reel_info(req: ReelRequest):
    try:
        shortcode = req.link.split('/')[-2] if req.link.endswith('/') else req.link.split('/')[-1]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        if not post.is_video:
            raise HTTPException(status_code=400, detail="In link reel ya video nist")

        hashtags = [word[1:] for word in post.caption.split() if word.startswith('#')] if post.caption else []
        tagged_users = post.tagged_users if post.tagged_users else []

        return {
            "link": f"https://www.instagram.com/p/{post.shortcode}/",
            "username": post.owner_username,
            "date": post.date.strftime('%Y-%m-%d %H:%M:%S'),
            "likes": post.likes,
            "views": post.video_view_count,
            "caption": post.caption,
            "hashtags": hashtags,
            "tagged_users": tagged_users
        }
    except instaloader.exceptions.PostNotExistsException:
        raise HTTPException(status_code=404, detail="Reel vojood nadarad")
    except instaloader.exceptions.LoginRequiredException:
        raise HTTPException(status_code=403, detail="Reel khosusi ast, login niaz ast")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
