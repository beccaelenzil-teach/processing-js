var drawing_on = 0

function setup() {
  createCanvas(1200, 800); 
  text('Drawing Off - Click mouse to turn drawing on.', 10, 30);
  fill(0)	 
}

function mousePressed(){
    if (drawing_on == 0){
    	drawing_on = 1;
    	text('Drawing On - Click mouse to turn drawing off.', 10, 30);
    }
    else{
    	drawing_on = 0;
    	text('Drawing Off - Click mouse to turn drawing on.', 10, 30);	
    }
    fill(0)
}

function draw(drawing){
  if(drawing_on == 1){
    fill(255,105,180);
    ellipse(mouseX, mouseY, 20, 20);
  }
  fill(0)
}