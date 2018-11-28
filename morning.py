import webbrowser
import time

sites = ["https://macfeber.se", "https://hd.se", "https://expressen.se"]


def open_tabs(theSites):
    for site in theSites:
        webbrowser.open_new_tab(site)


def main():
    webbrowser.open("https://tjock.se", new=0, autoraise=True)
    time.sleep(2)
    open_tabs(sites)


main()

