#@+leo-ver=5-thin
#@+node:2014fall.20141212095015.1775: * @file wsgi.py
# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:2014fall.20141212095015.1776: ** <<declarations>> (wsgi)
import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os
# 導入 random 模組
import random
# 導入 gear 模組
import gear

################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"

'''以下為近端 input() 與 for 迴圈應用的程式碼, 若要將程式送到 OpenShift 執行, 除了採用 CherryPy 網際框架外, 還要轉為 html 列印
# 利用 input() 取得的資料型別為字串
toprint = input("要印甚麼內容?")
# 若要將 input() 取得的字串轉為整數使用, 必須利用 int() 轉換
repeat_no = int(input("重複列印幾次?"))
for i in range(repeat_no):
    print(toprint)
'''
#@-<<declarations>>
#@+others
#@+node:2014fall.20141212095015.1777: ** class Hello
################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Hello(object):

    # Hello 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    #'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    #@+others
    #@+node:2015.20150621222226.1: *3* drawspur
    @cherrypy.expose
    # N 為上齒數, M 為下齒數, P 為壓力角
    def drawspur(self,N1=15,N2=24, M=4, P=20,midx=400):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
     
     <p> 

    <h3>齒輪數為介於 15-80 的整數</h3>
    <form method=POST action=mygeartest2>
    上齒數:
      <select name=N1>
    <option>15
    <option>16
    <option>17
    <option>18
    <option>19
    <option>20
    <option>21
    <option>22
    <option>23
    <option>24
    <option>25
    <option>26
    <option>27
    <option>28
    <option>29
    <option>30
    <option>31
    <option>32
    <option>33
    <option>34
    <option>35
    <option>36
    <option>37
    <option>38
    <option>39
    <option>40
    <option>41
    <option>42
    <option>43
    <option>44
    <option>45
    <option>46
    <option>47
    <option>48
    <option>49
    <option>50
    <option>51
    <option>52
    <option>53
    <option>54
    <option>55
    <option>56
    <option>57
    <option>58
    <option>59
    <option>60
    <option>61
    <option>62
    <option>63
    <option>64
    <option>65
    <option>66
    <option>67
    <option>68
    <option>69
    <option>70
    <option>71
    <option>72
    <option>73
    <option>74
    <option>75
    <option>76
    <option>77
    <option>78
    <option>79
    <option>80

    </select>

        
        <br />
    <br />
    下齒數:
    <select name=N2>
    <option>24
    <option>15
    <option>16
    <option>17
    <option>18
    <option>19
    <option>20
    <option>21
    <option>22
    <option>23
    <option>25
    <option>26
    <option>27
    <option>28
    <option>29
    <option>30
    <option>31
    <option>32
    <option>33
    <option>34
    <option>35
    <option>36
    <option>37
    <option>38
    <option>39
    <option>40
    <option>41
    <option>42
    <option>43
    <option>44
    <option>45
    <option>46
    <option>47
    <option>48
    <option>49
    <option>50
    <option>51
    <option>52
    <option>53
    <option>54
    <option>55
    <option>56
    <option>57
    <option>58
    <option>59
    <option>60
    <option>61
    <option>62
    <option>63
    <option>64
    <option>65
    <option>66
    <option>67
    <option>68
    <option>69
    <option>70
    <option>71
    <option>72
    <option>73
    <option>74
    <option>75
    <option>76
    <option>77
    <option>78
    <option>79
    <option>80
    </select>
    <br />
    <br /><br /><input type=submit value=畫出正齒輪輪廓>
    </form>

    <br /><a href="index">返回上一頁</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    #@+node:2014fall.20141215194146.1791: *3* index
    @cherrypy.expose
    def index(self):
        outstring = '''
     <!DOCTYPE html> 
     <html>
    <head>
    <h1></h1>
    <h2>學號：40223232</h2>
    <h2>姓名：陳敬奇</h2>

     <h3><a href="drawspur">個人齒輪</a><br />
       <h3> <a href="drawspur2">雙人齒輪</a><br />


       
    '''
        return outstring

    #@+node:amd.20150415215023.1: *3* mygeartest2
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def mygeartest2(self, N1=15, N2=24, M=4, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <br /><a href="index">返回首頁</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">


    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = 15
    # m 為模數
    m = 8
    # 第1齒輪齒數
    n_g1 = '''+str(N1)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(N2)+'''

    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2

    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(500,500)
    # rotate to engage
    ctx.rotate(pi)
    # put it back
    ctx.translate(-500,-500)
    spur.Spur(ctx).Gear(500,500,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(500,500+rp_g1+rp_g2)
    # rotate to engage
    ctx.rotate(-pi/n_g2)
    # put it back
    ctx.translate(-500,-(500+rp_g1+rp_g2))
    spur.Spur(ctx).Gear(500,500+rp_g1+rp_g2,rp_g2,n_g2, pa, "black")
    ctx.restore()


    # 按照上面三個正齒輪的囓合轉角運算, 隨後的傳動齒輪轉角便可依此類推, 完成6個齒輪的囓合繪圖

    </script>
    <canvas id="plotarea" width="1500" height="2000"></canvas>
    </body>
    </html>
    '''

        return outstring
    #@+node:2015.20150626160200.1: *3* drawspur2
    @cherrypy.expose
    # N 為上齒數, M 為下齒數, P 為壓力角
    def drawspur2(self,N1=15,N2=24, M=4, P=20,midx=400):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
     


    <h3>齒輪數為介於 15-80 的整數</h3>
    <form method=POST action=mygeartest3>
    上齒數:
      <select name=N1>
    <option>15
    <option>16
    <option>17
    <option>18
    <option>19
    <option>20
    <option>21
    <option>22
    <option>23
    <option>24
    <option>25
    <option>26
    <option>27
    <option>28
    <option>29
    <option>30
    <option>31
    <option>32
    <option>33
    <option>34
    <option>35
    <option>36
    <option>37
    <option>38
    <option>39
    <option>40
    <option>41
    <option>42
    <option>43
    <option>44
    <option>45
    <option>46
    <option>47
    <option>48
    <option>49
    <option>50
    <option>51
    <option>52
    <option>53
    <option>54
    <option>55
    <option>56
    <option>57
    <option>58
    <option>59
    <option>60
    <option>61
    <option>62
    <option>63
    <option>64
    <option>65
    <option>66
    <option>67
    <option>68
    <option>69
    <option>70
    <option>71
    <option>72
    <option>73
    <option>74
    <option>75
    <option>76
    <option>77
    <option>78
    <option>79
    <option>80

    </select>

        
        <br />
    <br />
    下齒數:
    <select name=N2>
    <option>24
    <option>15
    <option>16
    <option>17
    <option>18
    <option>19
    <option>20
    <option>21
    <option>22
    <option>23
    <option>25
    <option>26
    <option>27
    <option>28
    <option>29
    <option>30
    <option>31
    <option>32
    <option>33
    <option>34
    <option>35
    <option>36
    <option>37
    <option>38
    <option>39
    <option>40
    <option>41
    <option>42
    <option>43
    <option>44
    <option>45
    <option>46
    <option>47
    <option>48
    <option>49
    <option>50
    <option>51
    <option>52
    <option>53
    <option>54
    <option>55
    <option>56
    <option>57
    <option>58
    <option>59
    <option>60
    <option>61
    <option>62
    <option>63
    <option>64
    <option>65
    <option>66
    <option>67
    <option>68
    <option>69
    <option>70
    <option>71
    <option>72
    <option>73
    <option>74
    <option>75
    <option>76
    <option>77
    <option>78
    <option>79
    <option>80
    </select>
    <br />
    <br /><br /><input type=submit value=畫出正齒輪輪廓>
    </form>

    <br /><a href="index">返回上一頁</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </body>
    </html>
    '''

        return outstring
    #@+node:2015.20150626160220.1: *3* mygeartest3
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def mygeartest3(self, N1=15, N2=24, M=4, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <br /><a href="index">返回首頁</a><br />
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">


    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = 15
    # m 為模數
    m = 8
    # 第1齒輪齒數
    n_g1 = '''+str(N1)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(N2)+'''
    # 第3齒輪齒數
    n_g3 = '''+str(N1)+'''
    # 第4齒輪齒數
    n_g4='''+str(N2)+'''

    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2

    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(500,500)
    # rotate to engage
    ctx.rotate(pi)
    # put it back
    ctx.translate(-500,-500)
    spur.Spur(ctx).Gear(500,500,rp_g1,n_g1, pa, "blue")
    ctx.restore()
    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(500,500+rp_g1+rp_g2)
    # rotate to engage
    ctx.rotate(-pi/n_g2)
    # put it back
    ctx.translate(-500,-(500+rp_g1+rp_g2))
    spur.Spur(ctx).Gear(500,500+rp_g1+rp_g2,rp_g2,n_g2, pa, "black")
    ctx.restore()
    # 將第3齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of third gear
    ctx.translate(500+ rp_g2+ rp_g3,500+rp_g1+rp_g2)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g3+(pi/2+pi/n_g2)*n_g2/n_g3)
    # put it back
    ctx.translate(-(500+ rp_g2+ rp_g3),-(500+rp_g1+rp_g2))
    spur.Spur(ctx).Gear(500+ rp_g2+ rp_g3,500+rp_g1+rp_g2,rp_g3, n_g3, pa, "blue")
    ctx.restore()
    # 將第4齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合
    ctx.save()
    # translate to the origin of third gear
    ctx.translate(500+ rp_g2+ rp_g3,500+rp_g1+rp_g2+ rp_g3+ rp_g4)
    # rotate to engage
    ctx.rotate(-pi/n_g4+(-pi/2+pi/n_g3)*n_g3/n_g4-(pi/2+pi/n_g2)*n_g2/n_g4)
    # put it back
    ctx.translate(-(500+ rp_g2+ rp_g3),-(500+rp_g1+rp_g2+ rp_g3+ rp_g4))
    spur.Spur(ctx).Gear(500+ rp_g2+ rp_g3,500+rp_g1+rp_g2+ rp_g3+ rp_g4,rp_g4, n_g4, pa, "black")
    ctx.restore()



    </script>
    <canvas id="plotarea" width="1500" height="2000"></canvas>
    </body>
    </html>
    '''

        return outstring
    #@-others
#@-others
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }
    
root = Hello()
root.gear = gear.Gear()
cherrypy.server.socket_port = 8081
cherrypy.server.socket_host = '127.0.0.1'


if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(root, config=application_conf)
else:
    # 表示在近端執行
    cherrypy.quickstart(root, config=application_conf)
#@-leo
