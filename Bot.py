.failed = 0
        self.target = ''


    async def follow_target(self, token) -> None:
        session = aiohttp.ClientSession()

        async with session.put(f'https://social.xboxlive.com/users/me/people/gt({self.target})', headers={ "Authorization": token, "X-XBL-Contract-Version": "2" }) as follow_request:
            if follow_request.status in [200, 201, 202, 204]: 
                self.followed += 1 

            else:
                
        

    
    async def initialise(self) -> None:
        system('cls' if platform == 'win32' else 'clear')
        init(autoreset=True)
        print(' [\x1b[1;32m*\x1b[40m] @Wmeb xbox follower tool')
        if len(open('tokens/tokens.txt', 'r').readlines()) > 0:
            print(f" [\x1b[1;32m*\x1b[39m] Tokens: ({len(open('tokens/tokens.txt', 'r').readlines())}) \n")
        else:
            print(' [\x1b[1;31m!\x1b[39m] no tokens found in \'\x1b[1;33mtokens/tokens.txt\x1b[39m\'');_exit(0)

        self.target = input(' [\x1b[1;32m?\x1b[39m] target: ');print('')
        await self.start()


    async def start(self):
        await asyncio.gather(*[self.follow_target(user) for user in self.users])
        print(f" [\x1b[1;32m+\x1b[1;37m] XUID/GAMERTAG: ({self.target}) | followed: ({self.followed}) | failed: ({self.failed})", flush=True)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Follow_Bot().initialise())

