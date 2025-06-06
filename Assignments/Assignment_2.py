def setup():
    size(525, 750)
    background(223,203,170)
    rect_mode(CENTER)
    no_loop() 

def draw():
    no_stroke()
    fill(0) 
    rect(width / 2, 90, 170, 195)
    fill(37,191,203) 
    ellipse(433, 90, 160, 160)
    fill(0) 
    quad(350, 185, 525, 185, 525, 400, 350, 550)
    quad(175, 185, 0, 185, 0, 400, 175, 550)
    fill(162,112,183) 
    rect(width / 2, 248, 175, 125)
    fill(255) 
    rect(width / 2, 313, 175, 45)
    fill(241,26,60) 
    ellipse(192, 308, 35, 35) 
    ellipse(333, 308, 35, 35)
    no_stroke()
    
    
    fill(0) 
    rect(width / 2, 90, 170, 195)
    

    fill(37, 191, 203) 
   # ellipse(433, 110, 165, 165)
    
  
    grad_width = 174
    grad_height = 45 
    
    
    grad_x = (width - grad_width) / 2  
    
    grad_y = 250 + 86
    
    
    for i in range(grad_height):
        
        t = i / (grad_height - 1)
        
        
        r_val = int(lerp(254, 255, t))
        g_val = int(lerp(206, 255, t))
        b_val = int(lerp(232, 255, t))
        
        
        stroke(r_val, g_val, b_val)
        
    
        line(grad_x, grad_y + i, grad_x + grad_width, grad_y + i)
    fill(255) 
    rect(width / 2, 465, 174, 167)   
    triangle(175, 549, 350, 549, 175, 750)
    fill(28,50,149)
    triangle(175, 549, 175, 750, 0, 750)
    fill(0,146,117)
    triangle(350, 549, 350, 750, 175, 750)
    no_stroke()
    fill(232,8,42) 
    rect(437, 650, 175, 199)
    fill(0)

    
    push_matrix()
    translate(195, 325)
    rotate(PI/4)                    
    arc(0, 0, 35, 35, PI, TWO_PI, CHORD)
    pop_matrix()

    
    push_matrix()
    translate(330, 325)
    rotate(-PI/4)                   
    arc(0, 0, 35, 35, PI, TWO_PI, CHORD)
    pop_matrix()
    
    
    fill(241,26,60) 
    ellipse(262, 470, 23, 23)
    
    fill(225,26,60) 
    ellipse(262, 480, 33, 33)
    

        

  


