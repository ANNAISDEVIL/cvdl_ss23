import pygame

pygame.init()
input = "d1fferenœ"
noise = False
noise = True  
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# text_font = pygame.font.SysFont("Helvetica", 30)
text_font = pygame.font.Font("noto-sans.regular.ttf", 70)
#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

run = True
while run:

  screen.fill((255, 255, 255))

  draw_text(input, text_font, (0, 0, 0),30,60) # , 220, 150

  for event in pygame.event.get():
   if event.type == pygame.QUIT:
      run = False

  pygame.display.flip() 

# Save the screen as an image when the program finishes
if noise == False:
    pygame.image.save(screen, "./imgdataset/" + input + "notoSans.jpg")
else:
    pygame.image.save(screen, "./imgdataset/" + input + "notonoised.jpg")

print("Screen saved as " + input +".png" )

# next font
text_font = pygame.font.Font("TypographerTextur-Regular.ttf", 70)
run = True
while run:

  screen.fill((255, 255, 255))

  draw_text(input, text_font, (0, 0, 0),30,60) # , 220, 150

  for event in pygame.event.get():
   if event.type == pygame.QUIT:
      run = False

  pygame.display.flip() 

# Save the screen as an image when the program finishes
if noise == False:
    pygame.image.save(screen, "./imgdataset/" + input + "Typo.jpg")
else:
    pygame.image.save(screen, "./imgdataset/" + input + "Typonoised.jpg")

print("Screen saved as " + input +".png" )
pygame.quit()

