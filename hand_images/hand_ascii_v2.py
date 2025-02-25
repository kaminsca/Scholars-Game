class bcolors:
    BRIGHTMAGENTA = '\033[95m'
    BRIGHTBLUE = '\033[94m'
    BRIGHTCYAN = '\033[96m'
    BRIGHTGREEN = '\033[92m'
    WARNING = '\033[93m'
    BRIGHTRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GREEN = '\033[32m'
    GRAY = '\033[90m'
    YELLOW = '\033[33m'


empty = "\n".join([" " * 80] * 40)

L1 = """                                                                  **            
                                                                **+++*          
                                                              #***+++*          
                                                             #**+++++#          
                                                            #***++++*           
                                                           ***+++++*            
                                                         #***+++++*             
                                                        #***+++++*              
                                                       #****++++*               
                                                      #****++++**               
                                                    #****+++++*#                
                                           #****####***++++++*                  
                                #*********++++*####***++++++*                   
                          #*******+*#***+++++*******+++++++*                    
                         #****#****##****+++******++++++++#                     
                         ****##***###************++++++++*                      
                        #***####*###*************+++++++*                       
                        #***########***********++++++++*                        
                       ############************+++++++*#                        
                      ############*************+++++++*                         
                     %###########************+++++***+*                         
                     ##########**************+++++**++%                         
                    %#########************+********+++                          
                    #########**********************+++                          
                  ###########**********************++#                          
                ###**######**************************                           
             #*******####*************++***********#                            
           ##*********#**************+++*********#                              
         ###************************************#                               
       %###******************+++**************#                                 
     #####*****************+++++*************%                                  
   %#####*****************+++*************#%                                    
 %######****************++*************##                                       
#####******************+++**********##                                          
##**#****************+++****+*****#%                                            
#******************+++++********#                                               
*****************++++*********#                                                 
##************+*+**********##                                                   
##*********+*************##                                                     
###********************##                                                       
#********************##                                                         """

L2 = """
                                                     ***                        
                                                   ***++*                       
                                                 #**++++*                       
                                                #**++++*         #*+++          
                                               #**++++*        #***+=+*         
                                              #**+++++        #**+++++*         
                                            ##***++++        #**+++++*          
                                           ##****+++*      #***+++++#           
                                           #***++++*      #***++++*             
                                      #####**+++++*     ##**+++++*              
                                    ######**+++++*     #****++++*               
                                   ######***++++*    ##*****+++*                
                                  #**####*+++++*   %#***+++++**                 
                                #***###**++++++*####**++++++*#                  
                              ##***##****+++++++*****+++++**                    
                           %##****##****++++++******+++++*#                     
                          ####***###****++*******+++++++*                       
                         #####**###**+***********++++++*                        
                        ######*###**************++++++*                         
                       ##########***********++++++++**                          
                      ##########***********+++++++++*                           
                     ##*###*###************++++++++**                           
                    #######*##**********++++++++++**                            
                   #######*************++++++++++**                             
                  #######************+++++++++++**#                             
                 #*######***********+++++++++*****                              
               #***#####***********++++++++******                               
             ##****####***********++++++++******                                
          #********##************++++++++******#                                
        ##***********************++++++*******#                                 
      ###*******************++***++++++******#                                  
    #####*****************++++++***+*******#                                    
  %#####****************+++++++++++*******#                                     
%######****************++++++++++*******#                                       
######****************+++++++********##                                         
####*****************+++++********##                                            
##******************++++***+****##                                              
####**************+++++*******##                                                
######**********++++++******#%                                                  
######*********++++*******##                                                    """

L3 = """
                                                         #**++                  
                                           #***         #**+++*                 
                                          #**+**       #**+++**                 
                                         #*+++**      #**++++*                  
                                         **+++*      #**++++*                   
                                        #*++++#     #**++=++                    
                                       #*++++*     #**++=++           ##        
                                      %**++++    ##**+++=+         #**+++*      
                                      #**+++*   #****++++*        ***++++*      
                                     #***++*#  ##****+++*       #**+++++*       
                                     #**+++## #****++++*       #**+++++*        
                                    #**+++##%##**+++++#     %#**+++++*#         
                                   %**+++*###***++++*#    ##**++++++*           
                                   #**++*###***++++*    ##*****++++*            
                                ###**+**##****++++*    ##**+++++++*             
                              ####*****#*****+++++*#%##**++++++**#              
                            %####*****#*****++++++******++++++**                
                           ####******#****++++++++****++++++**                  
                          ######*********++++******++++++++*                    
                         #######********++*********+++++++*                     
                        #######*******++**********++++++*#                      
                      %##########************++++++++*+*                        
                      ##########************++++++++++*                         
                     #######***#**********+++++++++++*                          
                    ######***************+++++++++++*                           
                   #######**************+++++++++++*                            
                 ##**####***********++++++++++++++**                            
               #*****###*********+++++++++++++++***                             
            %##*****###********++++++++++++++****#                              
          ##********##********+++++++++++++*****#                               
       %##*****************++**+++++++++++****#                                 
     %###***************+++*++++++++++++******                                  
   %####*****************++++++++**+++******#                                   
 %####******************+++++++++**********#                                    
######*****************+++++++++++*******#                                      
###******************++++++++++*******##                                        
##*******************++++++********##                                           
##*****************++++++*******##                                              
###**************++++++*******##                                                
#*###*********++++++++******#%                                                  """

L4P = """                                                            ##                  
                                                    #***+*#*++++                
                                                   #***+++**+++*                
                                                  **+++++**+++++                
                                            **** **++++*#*++++***+*             
                                          #**++***++++***+++++**+++             
                                         #**++***++=+***++==****+++             
                                        #*+++***++=+***+++=+***++++             
                                       #*+++****+++****+++=+***+++*             
                                      **+++*****++#****++++**+++++              
                                    #***++#****++#***+*+++***++++*              
                                   #***++#**++++##**+++++****+++++              
                                  #**+++#**++++##**+++++#****+++*               
                                ##**++*#**+++*#***+++++*#****+++*               
                              ##***++******+*****++++++***+++++*                
                             #*****************+++++++***++++++*                
                           %*******************+++++****++++++*                 
                          %#*****************+++++++***+++++++                  
                         ##*****************++++++++*++++++++#                  
                        ###****************++++++++++++++++++                   
                      %###*****##********+++++++++++++++++++#                   
                     %###******##*******+++****++++++++++++*                    
                     ###***####********+*****++++++++++++++                     
                    ###****##********++*****++++++++++++++#                     
                   ####***#********+++*****++++++++++++++*                      
                  ####************++*****+++++++++++++++*                       
                %####************++****++++++++++++++++*                        
              ##***************++****+++++++++++++++++#                         
           ##*********************++++++++++++++++++*#                          
        ##**********************++++++++++++++++++**#                           
      ##********************+**+++++++++++++++*****#                            
   %###******************+++++++++++++++++++*****#                              
 %####****************++++++++++++++++++++******#                               
#####******************++++++++++++++++++******%                                
##********************+++++++++++**++++******#                                  
##*******************++++++++++++++++******#                                    
********************++++++++++++++*******##                                     
********************+++++++++++*******###                                       
******************+++++++++********###                                          
****************++++++++********###                                             
**************++++++++********#%                                                """

L4S = """                                                  #**#                          
                                                ##**++*                         
                                               #***+++*                         
                                              #**++++*                          
                                         #*+*****+++*              #**+*        
                                        #**++***++++*            #***++++       
                                       #**++***+==+*            #**+++++*       
                                      #**++***++=++           #***+++++***      
                                     #**++*#**+++++          **++++++**++++     
                                    #**++*#***++++        #***+++=++***++++     
                                   #***+*#***++++*      #***++++=+***+++++*     
                                  #***+*#**+++++*      #****+++++****++++*      
                                 #***+*#**+++++*#    #******++++**++++++*       
                                ##**++#***+++++*   ##**+++++++***++++++#        
                               ##**++***+++++++*###**+++++++*****+++++#         
                             %#********++++++++*****++++++*#*****++++           
                            ##********+++++*******++++++++**+++++++*            
                           %**********+*********++++++++***+++++++*             
                          %#*******************++++++****+++++++**              
                         %##*****************++++++++++++++++++*                
                        ###****##**********++++++++++++++++++**                 
                       ###****###********++++++++++++++++++++#                  
                      ###****###********+++****+++++++++++++#                   
                     ###****##********++*****++++++++++++++#                    
                    ###***###*******++******+++++++++++++*                      
                   %##*************++******++++++++++++++                       
                  ###************++*****+++++++++++++++*                        
                ####************+****+++++++++++++++++*                         
             #****#***************+++++++++++++++++++#                          
         %#*********************+++++++++++++++++++**                           
       ##*********************+++++++++++++++++++**#                            
    %###****************++++++++++++++++++++******#                             
  #####***************+++++++++++++++++++++*****#                               
#####*****************+++++++++++++++++++******#                                
###*******************+++++++++++**++++******#                                  
###******************++++++++++++**+********#                                   
#*******************++++++++++++++*******##                                     
*******************+++++++++++*********##                                       
******************+++++++++*********##%                                         
****************+++++++**********##                                             
**************+*+++++*********#%                                                """

L5P = """                                                        #**  #**++              
                                                      #**+++***+++*             
                                                     ***+++***++++*             
                                              #*** #**++++***++++***            
                                            ##*++****++++***++=+**+++*          
                                           #**+++**++++****++=+****++*          
                                          #**++***++=+****++==***++++*          
                                         **+++****+++#****+==****+++*           
                                       #**+++*****+*#****++++***++++            
                                      #***+*#***++*#*****++*#**++=+*            
                                    #***++*#**+++##**+++++*#***+++*             
                                   #**+++##*++++##**+++++*#***++=+*             
                                 #**+++*#***++*#***+++++##****+++*              
                              ##******************+++++****+++++**              
                             #*******************+++++****++++++*               
                            #******************++++++#***++++++*                
                          %##****************+++++++****++++++*                 
                         ###****************++++*+++++++++==++                  
                        ##*****************+++**++++*++++===+# #******          
                      %##****************++****++++*++++===+*##*+**+++*         
                     %###***##***************+++++++++++==+*#***++++++*         
                    %##****##***************+++++++++==+=+*#**++++++*#          
                    ###*************+******+++++++++++++=+#**++++++*#           
                  ####************++******+++++++++++++=+#*++++++++#            
                ##*#************++******++++++++*+++++=+**++++++++*             
             ##***##*****************+++++++++**+++===++**+==++**#              
          ###***********************+++++++++++++++===++++=+++**                
       %#************************++++++++++***+++++===++=++++*                  
     %##***********************++++++++++***++++++++++++++++*                   
  %####****************++**+*++++++++++++******++++++++++++*                    
%#####*****************+++++++++++++++++++********++++++++*                     
####******************++++++++***+++++++++***********++++*                      
###******************++++++++++++++++++++**********+++**                        
#*******************++++++++++++++******************##                          
*******************++++++++++++*****************##                              
******************++++++++*+++++*************##                                 
*****************+++++*+++**********########                                    
***************+++++***+++*****###                                              
***********++++++++********###                                                  
************++**********##%                                                     
*********************##%                                                        """

L5R = """






                                            #****                               
                                      ##****+++++++******                       
                                   ##***+++++++++++++++++#                      
                                 #***+++++++++***********                       
                              ##***++++++++***#####***+*#                       
                             ##***+++++++***#####**++++*#                       
                            ###***++++++**###***++++++***#                      
                           ###****++++++****##***++**+++++*                     
                          ###*****+++++****#####***++=++++*                     
                         ###*****+++++****##****++==+++++*#                     
                       %###******++++*****###**+++++++++*%                      
                      ####***************#%###*****+++++++                      
                   ######****************####**+++==++++++%                     
                %########***************###***++++++++++**                      
              ###########***************#####**++++++++#                        
           %######*******#*************+*####**++++++++*                        
        %####**************#**********+++*###*++++++++*#                        
      #####**************************++++++*###******#                          
    %###************+++++***********+++++++*#                                   
 %####*************++++++++********++++++*#                                     
####*******++++***++++++++**********+***#                                       
##********+++++++++++++++++**********#                                          
********++++++++++++*+++********###%                                            
*****+++++++++++++*++*******##%                                                 
*****+++++++++++**********#%                                                    
****+++++++++***********#                                                       
**++++++++++**********#                                                         
**++++++++***+******#%                                                          
***+++++**++*******#                                                            
***+++**++*******#                                                              
*******++******#                                                                
*************#                                                                  
************#                                                                   
**********#%                                                                    """

plumb_ascii = """                                                                                                    
                                                                                               #=---
                                                                                        ===--:::::--
                                                                                   +-:::::----==++**
                                                                              --::::----==+++*######
                                                                          ==::-----==++*###%%%%%%%%%
                     -:::-+                                           #-::::----=++*##%%%%%%%%%%%%%%
                   -:::-:::--::-=                                =-::::::----=+**#%%%%%%%%%%%%%%%%%%
                 =:::::::::---====*                       +=-:....:::::---=+*##%%%%%%%%%%%%%%%%%%%%%
              =::::::::---==**##**++                +-::::...:::::::--==++*##%%%%%%%%%%%%%%%%%%%%%%%
          +--::::::----==+*#######**++          +--::::::::--------=++**###%%%%%%%%%%%%%%%%%%%%%%%%%
       *-:::::----===++*############*++     =-::::-------=++++====+++**##%%%%%%%%%%%%%%%%%%%%%%%%%%%
   =--:::::----==+++**#####%%%%#%%%%#+=-:::--===++******###**+==++++**####%%%%%%%%%%%%%%%%%%%%%%%%%%
-:::::::::---==+++**#######%%%%%%%#*+==++++**##%%%%%%%%%%##++==++***###%%%%%%%%%%%%%%%%#%@          
::::::::--===+++***########%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%#+--=+**####%%%%%%%%#%##%%%%%#%            
----==+++++*****##****#######%%%%@@@%%%%%%%%%%%%%%%%%%@%%+-=++*#%%%%%%%%%%%%%#%%%%%%%%              
==++***###########*******#######%@@@@%%%        *=#%@@@@%++**#%%%%%%%%%%%%%%#%%%%%@                 
****###%%%%%%%%%%####***********##%%%%%        +=*%%@@@@#*#%%%%%%%%%%%%%%#%%%%%                     
########%%%%%%%%%%%%%%%%#######***#####*       *#%%@@@@@**%%%%%%%%%%%%%%%%%                         
%%%%%%#######%%%%%%%%%%%%%%%%%%#####%%##*      %%%%%%%%#*#%%%%%##%%%%%%                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       %%%%%%#**#%%%%#%%%%%%%%                             
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%           %%%#*#%%%%#%%%%%%%%                              
%%%%%%%@         @@@@@@@@                             %#%%%%##%%%%%%%                               
%@                                                     %%%%%%#%                                     
                                                        %%%%#%                                      
                                                        %%%%%                                       
                                                                                                    """

R1 = "\n".join(line[::-1] for line in L1.splitlines())
R2 = "\n".join(line[::-1] for line in L2.splitlines())
R3 = "\n".join(line[::-1] for line in L3.splitlines())
R4P = "\n".join(line[::-1] for line in L4P.splitlines())
R4S = "\n".join(line[::-1] for line in L4S.splitlines())
R5P = "\n".join(line[::-1] for line in L5P.splitlines())
R5R = "\n".join(line[::-1] for line in L5R.splitlines())


def combine_hands(l, r):
    return "\n".join(f"{original.ljust(80)}  |  {flipped.ljust(80)}" for original, flipped in zip(l.splitlines(), r.splitlines()))

def flip_upside_down(ascii_art):
    return "\n".join(reversed(ascii_art.splitlines()))

def combine_and_flip(l, r):
    l_flipped = flip_upside_down(l)
    r_flipped = flip_upside_down(r)
    
    return combine_hands(l_flipped, r_flipped)


hands_map = {
    "L10": L1,
    "L11": L1,
    "L20": L2,
    "L21": L2,
    "L30": L3,
    "L31": L3,
    "L40": L4P,
    "L41": L4S,
    "L50": L5P,
    "L51": L5R,
    "R10": R1,
    "R11": R1,
    "R20": R2,
    "R21": R2,
    "R30": R3,
    "R31": R3,
    "R40": R4P,
    "R41": R4S,
    "R50": R5P,
    "R51": R5R,
}