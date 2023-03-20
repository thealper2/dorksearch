import requests
import colorama
import argparse
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

def dork_search(site="", ext="", intitle="", cache="", related="", inpostauthor="", inanchor="", intext="", inurl="", link="",start_page=0, num_pages=1, results_per_page=10, file_name=""):
	dorks = []
	if site != None:
		dorks.append(" site:" + site)
	if ext != None:
		dorks.append(" ext:" + ext)
	if intitle != None:
		dorks.append(" intitle:" + intitle)
	if cache != None:
		dorks.append(" cache:" + cache)
	if related != None:
		dorks.append(" related:" + related)
	if inpostauthor != None:
		dorks.append(" inpostauthor:" + inpostauthor)
	if inanchor != None:
		dorks.append(" inanchor:" + inanchor)
	if intext != None:
		dorks.append(" intext:" + intext)
	if inurl != None:
		dorks.append(" inurl:" + inurl)
	if link != None:
		dorks.append(" link:" + link)

	dork_query = ''.join(dorks)
	print(f"{Fore.RED}--- DORK: {dork_query} ---{Fore.RESET}")

	for page in range(start_page, num_pages):
		url =  f"https://www.google.com/search?q={dork_query}&start={page*results_per_page}"
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
		res = requests.get(url, headers=headers)
		soup = BeautifulSoup(res.text, "html.parser")
		links = soup.find_all("a")
		for link in links:
			href = link.get("href")
			if href is not None and "http" in href and not "google" in href:
				if file_name != None:
					with open(file_name, "a") as f:
						f.write(f"[+] {href}\n")

				elif file_name == None:
					print(f"{Fore.GREEN}[+] {href}{Fore.RESET}")

	if file_name != None:
		print(f"{Fore.YELLOW}[-] Result: {file_name}{Fore.RESET}")


argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('--site', required=False, type=str, help='')
argument_parser.add_argument('--ext', required=False, type=str, help='')
argument_parser.add_argument('--intitle', required=False, type=str, help='')
argument_parser.add_argument('--cache', required=False, type=str, help='')
argument_parser.add_argument('--related', required=False, type=str, help='')
argument_parser.add_argument('--inpostauthor', required=False, type=str, help='')
argument_parser.add_argument('--inanchor', required=False, type=str, help='')
argument_parser.add_argument('--intext', required=False, type=str, help='')
argument_parser.add_argument('--inurl', required=False, type=str, help='')
argument_parser.add_argument('--link', required=False, type=str, help='')
argument_parser.add_argument('--out', required=False, type=str, help='')
arg = argument_parser.parse_args()

if (arg.site != None or arg.ext != None or arg.intitle != None or arg.out != None or cache != None or related != None or inpostauthor != None or inanchor != None or intext != None or inurl != None or link != None):
	dork_search(site=arg.site, ext=arg.ext, intitle=arg.intitle, file_name=arg.out, cache=arg.cache, related=arg.related, inpostauthor=arg.inpostauthor, inanchor=arg.inanchor, intext=arg.intext, inurl=arg.inurl, link=arg.link)

