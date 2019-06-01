import graphics
import requests
import datetime
import time


#get Data of Contest
def get(rid,live,upcoming):
    now = datetime.datetime.now()
    url = 'https://clist.by/api/v1/json/contest/?&order_by=-start&username=swiggy123&api_key=a0fc6e7ce627ee61b7fced4c976609b97bb65b76&limit=25'
    params = dict({
        'resource__id' : rid
    })
    resp = requests.get(url=url, params=params)
    x = resp.json()
    t = x['objects']
    n=len(t)
    now=str(now)
    for i in range(n):
         if(t[i]['start'][:10:] >now[:10:]):
            upcoming.append(t[i])
         if(t[i]['start'][:10:] == now[:10:]):
              if(t[i]['end'][11::]>=now[11:19] and t[i]['start'][11::]<=now[11:19]):
                   live.append(t[i])
              else:
                   upcoming .append(t[i])



#Loading Page
def load():
    global upcoming1 , upcoming2 , upcoming3 , live1 , live2 , live3
    r1 = graphics.Rectangle(graphics.Point(0,10), graphics.Point(10,0))
    r1.setFill('white')
    r1.draw(win)
    m1=graphics.Text(graphics.Point(5,8),'Contestia')
    m1.setSize(30)
    m1.draw(win)
    m1.setTextColor('blue')
    m1.setStyle('bold')
    m2=graphics.Text(graphics.Point(5,7),'Never miss any contest')
    m2.setSize(15)
    m2.draw(win)
    p1 = graphics.Circle(graphics.Point(3, 5), 0.2)
    p2 = graphics.Circle(graphics.Point(4, 5), 0.2)
    p3 = graphics.Circle(graphics.Point(5, 5), 0.2)
    p4 = graphics.Circle(graphics.Point(6, 5), 0.2)
    p5 = graphics.Circle(graphics.Point(7, 5), 0.2)
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
    p4.draw(win)
    p5.draw(win)
    m4=graphics.Text(graphics.Point(5,3),'Akshat Garg')
    m4.setSize(15)
    m4.draw(win)
    m5=graphics.Text(graphics.Point(5,2),'Suryaprakash Agarwal')
    m5.setSize(15)
    m5.draw(win)
    p1.setFill('green')
    p2.setFill('green')

    #data fetching
    live1 = []
    upcoming1 = []
    get(1,live1,upcoming1)
    p3.setFill('green')
    live2 = []
    upcoming2 = []
    get(2,live2,upcoming2)
    p4.setFill('green')
    live3 = []
    upcoming3 = []
    get(73,live3,upcoming3)
    p5.setFill('green')
    #data fetching over
    #win.close()


#Selection the Coding Platform
def init():
    global upcoming
    r1 = graphics.Rectangle(graphics.Point(0,0), graphics.Point(150,100))
    r1.setFill('white')
    r1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(50,4), graphics.Point(100,32))
    r1.setFill('white')
    r1.draw(win)

    m1=graphics.Text(graphics.Point(75,18),'Codeforces')
    m1.setSize(20)
    m1.draw(win)
    m1.setTextColor('red')
    m1.setStyle('bold')

    r2 = graphics.Rectangle(graphics.Point(50,36), graphics.Point(100,64))
    r2.setFill('white')
    r2.draw(win)

    m2=graphics.Text(graphics.Point(75,50),'Codechef')
    m2.setSize(20)
    m2.draw(win)
    m2.setTextColor('brown')
    m2.setStyle('bold')


    r3 = graphics.Rectangle(graphics.Point(50,68), graphics.Point(100,96))
    r3.setFill('white')
    r3.draw(win)

    m3=graphics.Text(graphics.Point(75,82),'Hackerearth')
    m3.setSize(20)
    m3.draw(win)
    m3.setTextColor('blue')
    m3.setStyle('bold')
    while(True):
        click=win.getMouse()
        if(click.x>=50 and click.x<=100 and click.y >=4 and click.y<=32):
            upcoming = upcoming1[::-1]
            break
        elif(click.x>=50 and click.x<=100 and click.y >=36 and click.y<=64):
            upcoming = upcoming2[::-1]
            break
        elif(click.x>=50 and click.x<=100 and click.y >=68 and click.y<=96):
            upcoming=upcoming3[::-1]
            break

    r1.undraw()
    r2.undraw()
    r3.undraw()
    m1.undraw()
    m2.undraw()
    m3.undraw()


#For redering the contests
def render():
    r1 = graphics.Rectangle(graphics.Point(10,80), graphics.Point(140,10))
    r1.setFill(graphics.color_rgb(232, 239, 244))
    r1.draw(win)

    r1 = graphics.Rectangle(graphics.Point(10,80), graphics.Point(140,70))
    r1.setFill('cyan')
    r1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(10,80), graphics.Point(60,70))
    r1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(60,80), graphics.Point(90,70))
    r1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(90,80), graphics.Point(120,70))
    r1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(120,80), graphics.Point(140,70))
    r1.draw(win)
    m1=graphics.Text(graphics.Point(35,75),'Event')
    m1.setSize(15)
    m1.setStyle('italic')
    m1.draw(win)
    m1=graphics.Text(graphics.Point(75,75),'Start Time')
    m1.setSize(15)
    m1.setStyle('italic')
    m1.draw(win)
    m1=graphics.Text(graphics.Point(105,75),'End Time')
    m1.setSize(15)
    m1.setStyle('italic')
    m1.draw(win)
    m1=graphics.Text(graphics.Point(130,76),'Duration')
    m1.setSize(15)
    m1.setStyle('italic')
    m1.draw(win)
    m1=graphics.Text(graphics.Point(130,72),'HH:MM')
    m1.setSize(8)
    m1.setStyle('italic')
    m1.draw(win)

    for i in range(min(6,len(upcoming))):
        r1 = graphics.Rectangle(graphics.Point(10,80-(i+1)*10), graphics.Point(140,70 -(i+1)*10))
        r1.draw(win)
        r1 = graphics.Rectangle(graphics.Point(10,80 -(i+1)*10), graphics.Point(60,70 -(i+1)*10))
        r1.draw(win)
        r1 = graphics.Rectangle(graphics.Point(60,80 -(i+1)*10), graphics.Point(90,70 -(i+1)*10))
        r1.draw(win)
        r1 = graphics.Rectangle(graphics.Point(90,80 -(i+1)*10), graphics.Point(120,70 -(i+1)*10))
        r1.draw(win)
        r1 = graphics.Rectangle(graphics.Point(120,80 -(i+1)*10), graphics.Point(140,70 -(i+1)*10))
        r1.draw(win)
        m1=graphics.Text(graphics.Point(35,75-(i+1)*10),upcoming[i]["event"])
        m1.setSize(12)
        m1.draw(win)
        t = upcoming[i]["start"].split('T')
        f = t[0].split('-')
        f = f[::-1]
        t[0] = '-'.join(f)
        m1=graphics.Text(graphics.Point(75,77-(i+1)*10), t[0])
        m1.setSize(12)
        m1.draw(win)
        m1=graphics.Text(graphics.Point(75,73-(i+1)*10), t[1])
        m1.setSize(12)
        m1.draw(win)
        t = upcoming[i]["end"].split('T')
        f = t[0].split('-')
        f = f[::-1]
        t[0] = '-'.join(f)
        m1=graphics.Text(graphics.Point(105,77-(i+1)*10),t[0])
        m1.setSize(12)
        m1.draw(win)
        m1=graphics.Text(graphics.Point(105,73-(i+1)*10),t[1])
        m1.setSize(12)
        m1.draw(win)
        sec = datetime.timedelta(seconds=upcoming[i]["duration"])
        time = str(sec)
        time = time[:len(time)-3:]
        m1=graphics.Text(graphics.Point(130,75-(i+1)*10),time)
        m1.setSize(12)
        m1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(2,94), graphics.Point(12,84))
    r1.draw(win)
    m1=graphics.Text(graphics.Point(7,89),"BACK")
    m1.setSize(12)
    m1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(138,94), graphics.Point(148,84))
    r1.draw(win)
    m1=graphics.Text(graphics.Point(143,89),"CLOSE")
    m1.setSize(12)
    m1.draw(win)
    r1 = graphics.Rectangle(graphics.Point(70,2), graphics.Point(80,8))
    r1.draw(win)
    m1=graphics.Text(graphics.Point(75,5),"NOIFY ME")
    m1.setSize(12)
    m1.draw(win)
def main():
    init()
    render()
    while(True):
        click=win.getMouse()
        if(click.x>=2 and click.x<=12 and click.y>=84 and click.y<=94):
            init()
            render()
        if(click.x>=138 and click.x<=148 and click.y>=84 and click.y<=94):
            win.close()
            break
        if(click.x>=70 and click.x<=80 and click.y>=2 and click.y<=8):
            win2= graphics.GraphWin('', 200, 100)
            win2.setCoords(0,0,20,10)
            r1 = graphics.Rectangle(graphics.Point(0,0), graphics.Point(20,10))
            r1.setFill('silver')
            r1.draw(win2)
            m1=graphics.Text(graphics.Point(10,5),"Notification Sent")
            m1.setSize(10)
            m1.draw(win2)
            time.sleep(1)
            win2.close()

upcoming1 , upcoming2 , upcoming3 , live1 , live2 , live3 = [] , [] , [], [] , [], []
win = graphics.GraphWin('Contestia', 1200, 600)
win.setCoords(0,0,10,10)
load()
#win = graphics.GraphWin('Contestia', 1200, 600)
win.setCoords(0,0,150,100)
upcoming = []
main()
