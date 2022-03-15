#!/usr/bin/python
# https://open.spotify.com/playlist/3RVyFChwid1oUMjfUa7AXb
# insert spotify developer app settings here
# https://developer.spotify.com/documentation/general/guides/authorization/app-settings/
client_id = ""
client_secret = ""

import tkinter as tk
import tkinter.filedialog
import requests
from authlib.integrations.requests_client import OAuth2Session
from authlib.integrations.requests_client import OAuth2Auth
from authlib.common.security import generate_token
import webbrowser

top = tk.Tk()
top.title('spotifyplaylistdl')

frm_err = tk.Frame()
frm_spotify = tk.Frame()
frm_spotify.pack()

# label for error messages
lbl_err = tk.Label(master = frm_err, width = 109, bg = 'red', fg = 'white')
lbl_err.pack()

# used for input link errors
def err_link(code):
    if code == 0:
        lbl_err['text'] = "PLEASE ENTER LINK"
    elif code == 1:
        lbl_err['text'] = "ISSUE WITH LINK, TRY AGAIN"
    frm_err.pack()

# spotify api authorization with pcke extension
def spotify_auth(): 
    client = OAuth2Session(client_id, client_secret,
                           redirect_uri = 'https://localhost:8000/',
                           code_challenge_method='S256')
    code_verifier = generate_token(48)
    authorization_endpoint = 'https://accounts.spotify.com/authorize'
    uri, state = client.create_authorization_url(authorization_endpoint, 
                                                 code_verifier = code_verifier)
    webbrowser.open(uri)

    # tkinter gui for getting spotify code/state for token from redirect uri 
    lbl_auth = tk.Label(master = frm_spotify,
                        text = "PASTE REDIRECT LINK AFTER SPOTIFY AUTHORIZATION HERE (https://localhost:8000/?code=...)",
                        pady = 10)
    lbl_auth.pack()
    ent_auth = tk.Entry(master = frm_spotify, width = 90)
    ent_auth.pack()
    
    def submit_auth(): 
        auth_link = ent_auth.get()
        if len(auth_link) == 0:
           err_link(0)     
        else:
            token_endpoint = 'https://accounts.spotify.com/api/token'
            token = client.fetch_token(token_endpoint, auth_link,
                                   code_verifier = code_verifier)
            request_playlist(token)

    btn_submit_auth = tk.Button(master = frm_spotify, text = "SUBMIT",
                                command = submit_auth)
    btn_submit_auth.pack()

# use spotify api to get tracks from playlist id
def get_tracks(playlist_id,token):
    auth = OAuth2Auth(token)
    endpoint = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id)
    temp = requests.get(endpoint, auth = auth)
    print(temp.text)

# used to advance gui to get spotify playlist information and save dir 
def request_playlist(token):
    # hide auth gui
    frm_spotify.pack_forget()
    frm_err.pack_forget()
   
    # create playlist request gui
    frm_playlist = tk.Frame()
    frm_dir = tk.Frame()
    frm_playlist.pack()
    frm_dir.pack()

    lbl_entry = tk.Label(master = frm_playlist,
                         text = "INSERT SPOTIFY PLAYLIST", pady = 10,
                         width = 80)
    lbl_entry.pack()

    ent_link = tk.Entry(master = frm_playlist, width = 90, bd = 3)
    ent_link.pack(side = tk.LEFT)
    def submit_playlist():
        frm_err.pack_forget()
        playlist_link = ent_link.get()
        if len(playlist_link) == 0:
            lbl_err['text'] = "PLEASE ENTER LINK"
            frm_err.pack()
        # check length of playlist id valid
        elif len(playlist_link) != 22:
            try:
                temp = playlist_link.split("playlist/")[1]
                if len(temp) != 22:
                    err_link(1)
                get_tracks(temp,token)
            except:
              err_link(1) 
        else:
            get_tracks(playlist_link,token)
    def clear():
        frm_err.pack_forget()
        ent_link.delete(0, 'end')

    btn_submit_playlist = tk.Button(master = frm_playlist, text = "SUBMIT", 
                                    command = submit_playlist)
    btn_submit_playlist.pack(side = tk.LEFT)
    btn_clear = tk.Button(master = frm_playlist, text = "CLEAR",
                          command = clear)
    btn_clear.pack(side = tk.LEFT)

    def selectdir():
        path = tk.filedialog.askdirectory(title = "SELECT DOWNLOAD LOCATION")

    btn_dir = tk.Button(master = frm_dir, text = "SELECT DOWNLOAD LOCATION", 
                        command = selectdir)
    btn_dir.pack()

# start application by requesting spotify authorization and loop gui
spotify_auth()
top.mainloop()

