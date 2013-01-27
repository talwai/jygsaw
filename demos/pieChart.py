from Sudikoff import Laptops

diameter = 0
angles = [30, 10, 45, 35, 60, 38, 75, 67]
lastAngle = 0

def setup():
  openCanvas(640, 360);
  setBackground(100);
  global diameter
  diameter = min(width, height) * 0.75;
  noLoop();  // Run once and stop
}

def draw():
  for i in range(angles.length):
    setFill(angles[i] * 3.0);
    drawArc((width/2, height/2), diameter, diameter, lastAngle, lastAngle + angles[i]);
    global lastAngle
    lastAngle += angles[i];
  }
}
