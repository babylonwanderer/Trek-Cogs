import os
import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO

try:
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
except:
    spotipy = None


class Spotify:
    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json('data/spotify/settings.json')

    async def _api_request(self, query):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(self.settings['client_id'], self.settings['client_secret']))
        results = sp.search(query, limit=5, type='track')
        return results

    async def escape(self, s):
        if s:
            return s.translate(str.maketrans({"[":  r"\[", "]":  r"\]", "(":  r"\(", ")":  r"\)", "{":  r"\{", "}":  r"\}"}))
        return s

    async def _save_settings(self):
        dataIO.save_json('data/spotify/settings.json', self.settings)

    @commands.command(pass_context=True, name='spotify')
    async def _spotify(self, context, *, query: str):
        """Search for a song on Spotify"""
        if self.settings['client_id'] and self.settings['client_secret']:
            r = await self._api_request(query)
            if r['tracks']['total'] > 0:
                items = r['tracks']['items']
                l = '\a\n'
                for i, item in enumerate(items, 1):
                    track = await self.escape(item['name'])
                    artist = await self.escape(item['artists'][0]['name'])
                    url = item['external_urls']['spotify']
                    preview_url = await self.escape(item['preview_url'])
                    if i > 5:
                        break
                    l += '{} **[{}]({})** by **{}**\n\n'.format('[:arrow_forward:]({})'.format(preview_url) if preview_url else ':stop_button:', track, url, artist)
                l += '\a'
                em = discord.Embed(title='Search results for "{}":'.format(query), description=l)
                em.set_footer(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/2000px-Spotify_logo_without_text.svg.png', text='Powered by Spotify (▶️ preview available ⏹️ no preview available)')
                await self.bot.say(embed=em)
            else:
                await self.bot.say('**I\'m sorry, but I couldn\'t find anything.**')
        else:
            await self.bot.say('**You haven\'t set-up your api yet. Please visit https://developer.spotify.com/my-applications/ to get your api credentials. Then use `{}spotifyapi` to set up this cog.**'.format(context.prefix))

    @commands.command(name='spotifyapi')
    @checks.is_owner()
    async def _spotifyapi(self, client_id: str, client_secret: str):
        self.settings['client_id'] = client_id
        self.settings['client_secret'] = client_secret
        await self._save_settings()
        await self.bot.say('Roger that!')


def check_folder():
    if not os.path.exists('data/spotify'):
        print('Creating data/spotify folder...')
        os.makedirs('data/spotify')


def check_file():
    data = {}
    data['client_id'] = None
    data['client_secret'] = None
    if not dataIO.is_valid_json('data/spotify/settings.json'):
        print('Creating settings.json...')
        dataIO.save_json('data/spotify/settings.json', data)


def setup(bot):
    check_folder()
    check_file()
    if spotipy is None:
        raise RuntimeError("You need to run `pip3 install spotipy`")
    n = Spotify(bot)
    bot.add_cog(n)
