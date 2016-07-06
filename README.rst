Flask app to embed a bokeh server app
=====================================

Trying to demonstrate push_session and autoload_server usage.

In one terminal, run bokeh server::

    $ bokeh serve --host localhost:5000 --host localhost:5006

In another window, run flask::

    $ export FLASK_APP=app.py
    $ flask run

Go to http://localhost:5000/

This fails to show any plot and the Chrome Developer Tools Console shows the following:

```
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:27 Bokeh: BokehJS not loaded, scheduling load and callback at Wed Jul 06 2016 12:08:04 GMT-0600 (MDT)
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:44 Bokeh: injecting script tag for BokehJS library:  http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:44 Bokeh: injecting script tag for BokehJS library:  http://localhost:5006/static/js/bokeh-widgets.min.js?v=4b0df507cbc8b1cb4f8ec960d6c9718f
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:44 Bokeh: injecting script tag for BokehJS library:  http://localhost:5006/static/js/bokeh-compiler.min.js?v=47e1cfffd831e5c4e1e3ea0702edd89c
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:37 Bokeh: all BokehJS libraries loaded
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:87 Bokeh: BokehJS plotting callback run at Wed Jul 06 2016 12:08:05 GMT-0600 (MDT)
bokeh.min.js?v=8654bbf…:3 Bokeh: setting log level to: 'info'
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:69 Bokeh: injecting CSS: http://localhost:5006/static/css/bokeh.min.css?v=12cad2d8ad9f63966dc6553746de780f
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:71 Bokeh: injecting CSS: http://localhost:5006/static/css/bokeh-widgets.min.css?v=522d6173498a389c7f74f0e675195da0
autoload.js?bokeh-autoload-element=080e13ee-72b7-4a0e-8f48-db617fb1ac99&bokeh-session-id=lIuBWFy9b8…:14 Bokeh: all callbacks have finished
bokeh.min.js?v=8654bbf…:67 Bokeh: Will inject Bokeh script tag with params {"elementid":"080e13ee-72b7-4a0e-8f48-db617fb1ac99","sessionid":"lIuBWFy9b8ewTqco5KYJhm1kUhq43SHeaKHG5uYuTTwc","use_for_title":true,"modelid":"f725c25b-795b-4a1b-8a4e-9e52b1e7547e"}
bokeh.min.js?v=8654bbf…:67 Bokeh: Websocket connection 0 is now open
bokeh.min.js?v=8654bbf…:5 Error rendering Bokeh items  Error: Did not find model f725c25b-795b-4a1b-8a4e-9e52b1e7547e in session
  at http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500:5:3816
  at C (http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500:30:2126)
  at O (http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500:30:2212)
  at A (http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500:30:2029)
  at MutationObserver.f (http://localhost:5006/static/js/bokeh.min.js?v=8654bbf09300c1ff666bcae026fa9500:30:639)
```
