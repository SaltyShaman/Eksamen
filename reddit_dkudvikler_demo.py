import requests
import json

#For at køre: python reddit_dkudvikler_demo.py





class RedditSubredditDemo:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.url = f"https://www.reddit.com/r/{subreddit}/.json"
        self.data = None

    def fetch(self):
        try:
            headers = {"User-Agent": "PythonDemo/0.1 (by /u/yourusername)"}
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.data = response.json()
            print("=== JSON hentet fra Reddit ===")
            print(json.dumps(self.data, indent=2)[:500], "...")  # viser de første 500 tegn
        except requests.exceptions.RequestException as e:
            print("HTTP‑fejl eller netværksproblem:", e)
            self.data = None
        except ValueError:
            print("Respons kunne ikke parses til JSON")
            self.data = None

    def analyze(self):
        if not self.data:
            print("Ingen data at analysere")
            return

        print("\n=== Forsøg på at udtrække posts ===")
        # Det normale path: data → children (liste af posts)
        listing = self.data.get("data", {})
        children = listing.get("children", [])

        if not children:
            print("Ingen posts fundet — måske er subreddit tom eller strukturen ændret")
            return

        for i, child in enumerate(children[:5]):
            post = child.get("data", {})
            title = post.get("title") or "<ingen titel>"
            author = post.get("author") or "<ukendt author>"
            print(f"Post {i+1}:")
            print("  Title:", title)
            print("  Author:", author)

        # Eksempel på et felt du måske forventer men som kan mangle
        first = children[0].get("data", {})
        maybe_url = first.get("url")
        if maybe_url:
            print("\nURL for første post:", maybe_url)
        else:
            print("\nFelt 'url' mangler i første post — skal håndteres sikkert")


if __name__ == "__main__":
    demo = RedditSubredditDemo("dkudvikler")
    demo.fetch()
    demo.analyze()
