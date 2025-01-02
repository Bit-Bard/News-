import requests
import json 
# import tkinter as tk


query=input("which news you are interested ?")                                   #user will enter the query for news
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-12-01&sortBy=publishedAt&apiKey=531648dd87ea458f8f5f773a8ddd6a35"#news api


link=requests.get(url)
news=json.loads(link.text)
i=1


for article in news["articles"]:        #articles in dictionary of news and title and discription is the key valsue of it
    print("number of news : ",i)
    print(article["title"])
    print(article["description"])
    i+=1
    print("-----------------------------------------------------------------------")


# window = tk.Tk()
# window.title("My News App")
# label = tk.Label(window, text="BREAKING NEWS\n",)
# label.pack()

# Create a button
# button = tk.Button(window, text="Your News!", command=lambda: print("Button clicked!"))
# button.pack()

#  Start the event loop
# window.mainloop()