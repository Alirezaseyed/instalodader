# 📸 Instagram Info & Downloader CLI 

In tool behet komak mikone ta betooni az Instagram etela'at begiri ya download koni — az profile, reel, story, highlight ta hashtag va location.

---

## 🚀 Features

* 🔍 Get profile info (username, full name, followers, followings, post count, bio, status)
* 🎥 Get reel info (link, date, likes, views, caption, hashtags, tagged users)
* 🌐 Test reel link (check accessibility)
* 🖼 Download profile posts
* 📚 Download stories va highlights
* 🏷 Download tagged posts
* 🔖 Download posts by hashtag
* 📍 Download posts by location ID

---

## ⚙️ Installation

Aval Python 3.x ro nasb kon.

Ba'd file `requirements.txt` ro ba in mohtava besaz:

```
instaloader>=4.10
requests>=2.30
```

Ba'd in command ro bezan ta hame library ha nasb beshan:

```bash
pip install -r requirements.txt
```

---

## 🧭 How to Run

File ro save kon ba name `main.py` va ejra kon:

```bash
python main.py
```

Bad az ejra, ye menu miyad ke mitooni az bein gozine ha entekhab koni.

---

## 📋 Main Menu

```
1. Estekhraj etelaat account
2. Estekhraj etelaat reel (az rooye link)
3. Test link reel
4. Download posthay profile
5. Download storyha
6. Download highlightha
7. Download posthay tagged
8. Download posthay hashtag
9. Download posthay location
10. Khorooj
```

Har gozine baraye ye kar khas hast:

1️⃣ Info profile ro migire

2️⃣ Reel link ro check mikone va etela’at midah

3️⃣ Test mikone ke link kar mikone ya na

4️⃣ Hame post haye profile ro download mikone

5️⃣ Story ro download mikone

6️⃣ Highlight ro download mikone

7️⃣ Tagged post ro download mikone

8️⃣ Hasteg post ro migire

9️⃣ Post bar asas location ID ro migire

🔟 Exit

---

## 💾 Output Files

Har file info ya download shode tu ye file ya folder zakhire mishe:

* `{username}_profile_info.txt`
* `{username}_reel_{shortcode}.txt`
* Folder baraye post, story, highlight va ...

---

## ⚠️ Important Notes

* Agar profile private bashe bayad login koni.
* Instaloader tool az session va sleep estefade mikone ta block nashi.
* Be ghanon ha va rule haye Instagram ehteram bezar.
* In tool faghat baraye karaye research va educational estefade mishe.

---

## 🔑 Login (Optional)

Agar mikhay be private profile ha dastresi dashte bashi, mitooni login koni:

```python
import instaloader
L = instaloader.Instaloader()
L.login('your_username', 'your_password')
```


