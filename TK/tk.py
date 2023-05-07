from tkinter import *
import json
import os
import webbrowser

list = []

root = Tk()
root.title("Youtube Downloader")
root.geometry("500x320")
mylabel = Label(root, text='YouTube Downloader', pady=10)
mylabel.grid(row=1, column=1)
e = Entry(root, width=50, )

e.grid(row=2, column=1)

kk = e.get()


def all():
    command = f'yt-dlp "{e.get()}" -j'
    output = os.popen(command).read()

    videos = json.loads(output)

    for i in videos['formats']:
        if i['ext'] == 'mp4' and i['audio_channels'] != None:
            def callback(event):
                webbrowser.open_new(event.widget.cget("text"))
            resolution = Label(
                root, text=f"Resolution:{i['format_note']}",  width=50)
            title = Label(root, text=f"Title: {videos['title']}")
            lbl = Label(root, text=f" {i['url']}",
                        fg="blue", cursor="hand2", )

            lbl.bind("<Button-1>", callback)
            resolution.grid(row=4, column=1)
            title.grid(row=5, column=1)
            lbl.grid(row=6, column=1)


Label(root, text=kk)
Button(root, text='Download', padx=3, pady=5,
       command=all).grid(row=3, column=1)


# output = os.popen(command).read()

# videos = json.loads(output)
# videos
# for i in videos['formats']:
#     if i['ext'] == 'mp4' and i['audio_channels'] != None:
#         # print(i['format_note'], i['url'])
#         list.append(i['url'])


# def command_download():
#     url = Label(root, text=list[0])
#     url.grid(row=4, column=3)
#     url = Label(root, text=list[1])
#     url.grid(row=5, column=3)
#     # on_next = Button(root, text='Download', padx=3, pady=5,
#     #                  command=lambda: command_download(number+1)).grid(row=3, column=3)


# Button(root, text='Download', padx=3, pady=5,
#        command=command_download).grid(row=3, column=3)


root.mainloop()
