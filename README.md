# Python-Youtube-TimeStamp-based-playlist-extension-for-Streamlabs-OBS
Usage:
```bash
pip install -r requirements.txt
```
That will install selenium and urllib3, that are used on the project.
Then run the following on prompt or just execute the run.py.
```bash
python run.py
```

# What it does?
At run.py you can insert and start URL, but after the webdriver starts you can pretty much acess any playlist you want.
It supposed to save the current song being played by a long playlist video that show timestamps on description like that:

![aa](https://user-images.githubusercontent.com/56324869/97098775-a6bc6200-165f-11eb-876c-3bf478424745.png)

Then create a Text GDI+ source on stream and put the file in the folder called current_song_to_OBS.txt, it will be something like that:

![lul](https://user-images.githubusercontent.com/56324869/97098809-129eca80-1660-11eb-9a99-97338011c6f7.png)

in the end it will look something like that:

![song](https://user-images.githubusercontent.com/56324869/97098846-89d45e80-1660-11eb-88ca-a48a82d417ec.png)

you can find a clip of it running right here:
https://www.twitch.tv/nanohanana/clip/CalmPlausibleEndiveUnSane
