

web_header = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <link rel="shortcut icon" type="image/png" href="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQEhIREhIWEBUVFRUVFRgXFRUQFRYVFxcWGBcWFhUYHSggGR0lGxUWITEhJSkrLi4uGB8zODMtNygtLisBCgoKDg0OGxAQGy0lICYtLS0zLy0tLS0vLS0tKy0tLS0tLS8tLS0tLS0tLS0tLS0vKy0tLS0tLy0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAABAUDBgECBwj/xABGEAABAwEEBwQGCAMHBAMAAAABAAIDEQQFEiEGMUFRYXGBEyKRoQcyQlKxwSMzYnKCktHwFKLhQ3OywtLi8RY0U6MVFyT/xAAZAQEAAwEBAAAAAAAAAAAAAAAAAgMEAQX/xAAqEQACAgEEAQQBBAMBAAAAAAAAAQIDEQQSITFBEyIyYVFCcYHBIzOxFP/aAAwDAQACEQMRAD8A9xREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREJQBcEqJNbwMm97js/qopkc7WaoCwdaWjjyWqaQaamGQQQRCeQkA1JABOTRkMyTsVle9q7GF7wKkDuje45AdSQOq8/sFYJDM9plkoS32QZHa3OdsAFdVTmKDLLbpaFNOUlnHj8sz3XbWopno8VukZGO3cztKVeIwQ0cBUnUMqk568tS168tOY2VEQMpG0Zt/NUN8CVr7LPa7weW+uAcxmyBnMe0edTyW33PolZ4aOkHbvG1w7gP2WaupqpSpqp/2PL/AAjisnZ8Fx+WUNlvu+LVnBG1jfeIq38zqV6VWyXfHeYoZrTC7eBAXfzBzfgrui4IWadqlxGKRbGDXbbOBaHDXQ9CPmuW2wbRTzWNwWJwVJYWEcrXajVd1oukWlUdmOCMdtLuBoG8SVzofphabQ4sngq2v1sfqs4PDjnzbU8Nqu9CzZvxwQ9SO7b5N5RY4Z2v9U1/e5ZFSTCIiAIiIAiIgCIiAIiIAiIgCIo9ttbYm4ndBtJ3BAd7RO1gxONPieAWjX5pv9OyBrMMQcO2e7WQagUA1AOo4k7ArOa1Oldid0GwDcFqukt10f2tKtd3XcKnKvCpI6hadLCE57Z+Sm6UoxzE3eMLi12xsQzzJ1D5ncFr2jF5PDDBIC57G1jcfbjGQqd7agHoq28pHTEucfo9p/8AJ/s+PLWhppOzYyMtRFQ3GzWGUWwiubAcVdjiNQYPdzrXbQc1Mn0fikIqSGbQNZ4V2LXLBanxkNIw90OA1EAkgV3erqW1aO2jtLOx290h/wDY9W3KVSzB8FNWLZPeuSZZ7OyNoYxoY0agBQLIiLCbgiIgOrgtW0uvwwjsovrHfyjaT+9w4i7vy8m2eJzzr1NG0nl1HUhaBZLDJaZqH13nE868LdwPlzqVs0tKk3OfxRnvscfbHtmLR7R82lxe8nswe87a924H901Bb2yBsbQxjQ1oyAGQCkQWdsTGsYKNaKBdJFXqNQ7ZfXhE6qlBfZGxlpqDQhWl33oH0a/uu2bj+hVVIokoWcsNyRUdz3vUiKQ56mu38DxV4h0IiIAiIgCIiAIiIAiIgMdombG0vcaACpWm2y3unfiOQ1NG4fqs2lF5439i091h73F+7p8a7lWwocJ8KzzOjwkSZtOVNda7KKNG4AVOQGZWv3jb3TSYGEgb/dZv+87Zu6K2muU5YRCyahHLNuuO7oJGuy7RrXENryoQd+stO/NHxWd1owOoHNo5jDkHfaHvU3bFW6PSGQ4R3Yo+6aVGJ1PVBGwbeK6X3Yi+jJCaVrFK3JzXbM9jvI+S1uLc3HdyY09sFPZxk7Xqytpf/ds/xyq30Od/+VnB8w8JpFBuywzyGs3ecGhheNTwCSHU2GjsxvCtbgsxiZIw7JpCOTiHf5lC+S9JR8rH9llK/wAspeGWaIixGwISiqNJbcY4sLfXk7rRz38N/AFSjFyaSOSaSyzW78tnbyud/ZxZN4u/pXxPBXuj139lHicO+/N3AbAqm6rAHyMj1tjo553u1ivGve8FtbitmqmoRVUf5MunTm3a/wCDG9YJFleVgeVhNRHkUWVSZSospQEKZbVcF8stLXtBpJEWtkadeYq1w3hw27wRsWqzLV7XeUtjt0csTsONgY/UQ4YjkQdeYarK4b219EZS28ns6KJddubaImyN2jMbjtClqsmEREAREQBERAFXX/eP8PC5/tHus+8dXhmeisVoOnF4Y5xCDlGM/vuofIU8SgKqF1deanwlVsBUi0WsRMLtuocTsRLJwxX5eOEdm3M5VA2k6m/MqHYrM4lsTT9I/vPd7o9p3wAHJV0EmIumcagVw8Ttd1OQ/qtvuCxmNhe/6yShdwHss6DzXp8aarP6mYmvXsx+lF1YYGxMaxgo1ooP1PFTWAOGFwBB1g5hQo3KQxy83Lzk2lrYogwYQa7q55bqqHfFtdZ/pMBkZTvhvrNp7VNop8Oqj2y1FjMfulpPKoxeRKgW+8HdpEzEG9oXNaSKjtAKta7aKgOFRtprV9de/wBz6M9lmx7YrnwW13XnDaG44nh427xzGxTMS0K2XSWydpC42O0ZnL6uTfqyNeHUKdd+lrmOEVtj7F+x4zjfxy+XUBLNPKPK5RKu+MuHw/wbfiWnXhau1mklPqRAtbxdTOnQgc3OV/eFtAhdI0h4Le7hIIdXUARvOXVUFjshLooTnT6SQ7zWvm6p6KzSxSzY/BXqW3iteS7uSzGOOrvWecTuZ2dNSmOcuC5Y3OWWcnKTkzTFKKwjh7lgeV2e5YHuUTpjkKiylZpHKNI5ARpitK0zdR8TtwcfAtK3GYrTNMjV0f3XfELVo+bl/P8AxlV/wZvOhF59nL2Lj3ZNXB41eIy6Bb+vF2SFoY4GhAa4HcRQg+K9duq2ieGOUe20Hkdo6GoWefyZZHoloiKJIIiIAiIgOsjw0FxyABJ5BeOzWoyyPkOt7nO8TWi9L0wtXZWOd29uAfjIZ/mXlEDkOFtC5U982syPEbTkKj/UfkpdotPZsLtuoczqVFZX0DpDnXJvHd4n5LZoqt88vpFGontjx2bBctmEkgFO5FQncXeyOmtbexypLms/ZRtafWPefxcdf6dFascqtTd6tjfjwSpr2QwT2OWZjlCY9ZmvVBaSy0PDmHU5paeRFFrV943WXtB9ZCWyD78Tu98HLYGPUK0MAklYfVf3xyeKOH5gT+JbdJLuLMerWEprwyzjljtEbXEB7Hta4bciKg+ar7ZdVQW0E8Z1tfQuHJx19c+KgaGzkRPszj3rPI6PmwnEw+Bp+FX758ALjsFVVGydUnEvlXC2KbMFx3AxgOFzgzE1xY4VIc2tMznTOuddQzWO0W6CzTPbISxzqUJBw0Gqm8cRvKwWK/HMjc+ub3Ubt20FB4nqpN82F07SO7MNrXUB6HV8OaucXu2zeEymL4zFZaJcc7XgOa4OB1EEOB6hdXOWiyWCWzPJhkfZ3e4+paeVdY/MFLh0pljytMWXvszHMjV8OSrs0dkeVyvoshqIS46f2bU9ywPcodkveCb6uQGuzUfA6+izPcsrWC84kco0jl2kco8jkBhmctK0skrJTdGPMu/RbfK5aVfX0loc3eWM8QPm5bNCv8ufwmUaj4YLu1Nwho+yFu3ozt2KKWEnON+Ifdfs/M1x6rTL6d3yNwCsfRta8NsLNkkbh1aQ4eQcss37mXI9VREUSQREQBERAan6THOFjy1GVgdwHePxDV5pA9ejeli3CG7pNVXSQtA2mkjXOpxwtK8wsswcAQagio5LrTxkjnnAvm0Vowfsn9Bmst0xB8rG+zGA889TB459FTWufFJXr46vIea2PRtlIy863mvQZNHz6r0G/S032zNjfb9I2aN6kseq6N6ksevONRPY9ZmvUFj1ma9ATWvWO8D3WSe4cLvuvoP8Qb5rE16yto4FjtTgWnqrKZ7JpkLIb4uJRmb+Ht0cmplob2L/AO8bnGfi3qrTSG0kRYQaF5DR++ZCpL4s7pYXxnKRpyO6RhqCOdPNG3gbSIJCKdwucNzxVpH5sX5V6Fmn3XRfh/0Y6rdtTT7RLszA6eGMerGMZ/Dk3zWx9otfuAVMsvvOwj7rf6nyVsXrJq57rX9cGjTw21omPtOIYXtEjdzgCq203PZ5Pq3mE7j32eeY8eiyF6xueq677K/iyydcZ/JGvXjotK2rhGH/AGojn1bkT4FVjbZaoDhEhNPZkFD5jLoAtyFoc3USOS5ltoeMMrGSj7TQf6LV/wCyE/8AbBP9in0HH4SwaqzSZw+siPNuY8Mz8FnZpBZ3ZY8J3OFD4KxtN3WGT2Hwn7DqjwNR5KrtOjMTvUtA5PaP1HwTZpZ9Sa/c7m6PaTJkD2Seq4HqFr1ksJktTDTJ0rn/AIWkuHk0Kc3RowtdKTCWtFSQSCRuFG6+qyXjCbS0iEjuAVOIsoHVAGXI5cFdRVCCk1LOVjP4M91s3OMdpBviYY3kka942ZLP6O545Lyha19S1sj8hUGjC2hP4vJaparkIPfc3pVx86K/9GsUcd52ZoriIlNa0NBG/XTZlq4cFknVBZ5yzVGcnjg92REWUvCIiAIiIDRvS5CH2WIHUZw0/ijkp5hePXfI+B7oX6qkfdJ9ofZOv9le3elGz47vlIFSx0b/AOcNJ8HFea2GzR2uMOJDJoRWp1PYM6H9/FadPKL9k+ii5Ne6PZQS2VznkD2nUbx2AhbdC3AA0agAB0UeZ4aGyYQ7AQ6laVHA9a9EbeMUxqw57WnJw5j5jJX6+DW3C4Rn0Vqmm/OS0jepDHqtjkUhki883Fix6zNeq9kiytkQE9si7tkUJsi7tkQE+0WLG5so9ujXffGo9R8AuztHDGxzmjXU03VJPxcT1U+5bS0NOLVr5UzqrG8ZqwvwODSWnCTQiuzLattepswkvBksohltvs1yOydgxrNw8zmVwZF2lvNk8bZG5VGY91wyc08ioRkWOWc8mtdcEgyLo6RYDIsbpFwGZ0ixOkWJ0ixPkQHeR6jSPXD5FhNTqQFXf1rLWtaPadU8m5/HCpVzzFlkkkOuRxA5Du/6lRX6XOlLQK4QGAfaOZ+LR0UjSK92RRx2WAiQxgB7tbQ4Cmv2jXFWi9FQkqFBdvky7k7HJ+OCFeluEY3uOob+J3BdtAY3ut9lkJOIztoRlkM304YQW8iVS2WyOmJe4nD7TjrPAfvJbl6NYe1vKCgo2Nsj6bgGFo83hUTSqjjyycW5vPg91REWU0BERAEREBBv2w/xFnnh/wDJE9g5lpAPjRfP112wxxz7D2bhyNHL6PXz9p5dpslstkYFGyAzM+7JUnwdjHRWVfNEJ9HbRm1RWhksE8nZ5M7N+41NQ7YQcvDWqy+7mtFmdWRtW17sjK4eHeGbTwPmqu5pKYui2y6L+lhGHKSM5FjsxTcN3wW2erlGbT5Rmhp47U1wyqsV8ytydSUflf46j5c1dWW+YXUBdgO5/cPQnI9CpTrnu615wvNilPsnOMngCaeBHJV1v0VtkFax9szfH9IKcWet5J6ent+Lwzu62HayXbJFlbItKi7hIY58RGsAltObDl5KbFedob7TJPvNwnxbl5KE9Bavjhko6mD74NsbIu4kWtR364etCfwPa7ydRSI7+iOsSN5xuP8Ahqs8tPbHuLLVbB+S+tNuMcTyNtG/mIHwKii+Hua8jMMwYuGPEGnlVtOoWG0SxzQt7N4ccdXChaQA00q1wBpU+SjXLaoYZJ2zva1sgbG4OcG90AnF4uW+jFVG5rnJjuirbdv4RisN4mKYgn6OY9Gyf7v0V+ZFrtpuwOLow4SN9l7SHAj2XAjb86qws1uY1mGd4ZI3I1r3qanDmq9bR7vUh0y3T28bJdosDIujpFTy37ANTnO5Mefko0l/t9mKR3MNZ8SsapsfUWaHOK8l66RYnSLXpL5nOpjGfecXnwFFCntUzvWlNNzAIx4jPzV0dDbLtYK3qII2K1W1keb3hvM/JdLHfQcQ2KMvJ9p/cYONNZWt2SwPlP0UTpDvALvF51dSpt4WOWxCN0jmte8nCxpxOAAzc46tZAoK61oho64vE5Zf4KZ3za9iJV92ZtMque5xrSpxE1JoOaq47hLe/OcDfd2ngaauQz5LZLnt3Z2V9ofnJIaMrrDRkKcCcR4gBa1b7W6Q4nGp+HIbE1Oq2+yPg5RRxukzHbbSD3WjC0ahqW+ehKw4pLVaCMmtbE08XHE7yazxXmkz1716Mbp/hbvhqKPlrO/m+mGvJgYOi81tt5ZsSNrREXCQREQBERAF596X7k7WBlqaO9DVr+MT6AnjhdhPIuXoKx2iFsjXMeA5rgWuB1FpFCD0XYvDycayj5Tu19MQ3U+f6K2ilWTTHRma7LU5jweykLjC/Ih7QQTWmpwrmOO5VscqndzLJXXwsFzHMre7r9nh9SQge6e83wOrotYjlUhkyrLDeP8AqWGYAWqzMl4gAkcg7V0K4N33TN6r32Y7qmn8+Iea01s6yttCthdZD4shKEZdo2t2hgdnDamScCPm0n4KN/0ja2H+zfyfT/EAqJtoUuG9ZW+rK8cnGnhVaI6+1dlT00GbTYh/D1ZMAx9AdbXZZ7QTuKgXrd80nfZC5zXAOaQAQQRUEKgvy9HGU1NSGMB8MX+ZWFh0jtDIo2B+TWtAqGnKmrUtVmodcYz8syV6WLnLktbju6ZpFYHj8NM1Iva2x4CKgnzFNarGaVWge0Pyt/RV99WntQZmZH+0bx94fP8A5UadUrLPdwLtHhboszuuG0yUc1rcJzBxsIIO0UJWWLRC0H1pI2DgXPPhQDzWtWK+JYCQ2RzY3GpAJGEnaNysJbc5/rPLuZLviuX6u6uW3gvqprksl2NGrKz661V3huFnl3iucd2Q+pCZjvfVw/n1dGrXDOsbplinqrZds0KqC6RsVr0mlIpGGxDZQVI8cvJaTbbRJap83FxcQwEmtANZ5ays942vCw0OZyHzPgsVxNDcUx2DC35n5eKs0/Cc2Qs5aii4vi0gBkTcmsAAHSg8viqSWRczzEkk7VDlkWWTy8lyWC50RuY2+2Q2fWwnHLwibQu8cm83BfSQFMhktC9EWjX8LZjaZBSW0AOodbIhmxvAmuI82jYt+XCQREQBERAEREAREQFJpjo7HeNmfZ30DvWif7korhdyzII2gkL5stEMkMj4pGlj2OLXNOsOBoR/VfVy8w9LmhD7QP46zNxSsb9MwCrpGDU9o2uaNm0aswARw8jZIszZFXRy1Ulj0OEwSLuJVGaV2CYBKEq7iZQ6rs0odO15TVled5A8AB8lLEypppKyH73zU3EtmqeVFfRRT2yb267RWstNR/yNygYkxLGXma8IBTtI/V9oe6f0UWy2zD3Scth3f0WeKYtNR13Hmo1ssoNXR9W7Ry3hbo2q2O2ZmlBwe6JPMq6GRVNltZbkc2+Y5KfaiMHcOLFtGdBtruOz/hUPTy3YRZ6scZIM8hlkDW8h8z+9ysZ3hoEbdQCjWKDs29odbh3eX9VhklU7pJLYjlaz7mdpJFt3ox0RN4T9tK2tmhILq6pJBmI+I1F3Cg2ql0P0YnvOcRR1ZG2hlkpUMbw3uOwddQK+jLnuuGyQx2eFuCOMUaNZ4knaSaknaSspcTEREOhERAEREAREQBERAEREB5X6SPRn2xfa7C0CU1dJCKNbIdro9jX7xqdwNa+Oh5aS1wLXAkOBBaQRrBBzB4L62Wn6b+j6y3mDJ/29opQTNANaahK3LGPAjYUOHgcT1JaudJNGrbdj6WiOjCaNlbV8T91HbD9l1CoUFqBXUzhPwpgXEcoKzNIUsAoXSd/8XzVzgWv2vuvcNxK2aAhzWneAfJW2vOCmrjJiwLnApGFc0VWC4j4EwrOVgmkDQSTQDWmDhgtMMdC93dI2jWeFNqyG0AMJYKgZZZ5qktNqMrtzRq/U8VIhmc4tijaXucaNa0F7nHcGjMlba9Q6o8mSdKslwJ7zkdk9od4sP6LeNBfRxNeDRPaMVlgcKspQyyg+00EUa37R17BTNWuhnonlkLZrxJjbrEDXd53969vqj7LTXiNS9jijaxrWtAa1oAaBkAAKAAclksnGXSNUINdshXFcsFihbBAzAxvVznHW5ztrjv8AkrBEVRYEREAREQBERAEREAQohQHUuWF9oAWYtWJ8AKAg2i8w1VNr0kwq4nuwOVZadGw5Aa5eOl1WuY5oe0ijmuAc0jcQciF5df1gsj3F8LTZz7re9H0afV6GnBeu2rQrEqi0+jouQHi7nvjOuvJZ4rzO1em2n0XPKr5fRRLsQ5g83t8ge7ENutWF2XgBGGnW3LpsW4u9FE+8rp/9U2jeVLcQ2YeTXP8A5Jm9dXXo1bKPRTaPePl+iys9FM20krm5ksGnSXruChWh8stMjTYPmV6RF6L5QpsPo2kC6pYOOOTzq7blDiO0fhG0NzcepyHmvSdFbXZ7GKWeFrCcnP8AWkdzec6cNSm2f0fuCtrLoaWrjbfZJJLonWTSFzlb2e9C5QbNo7hVnBdgauHSTHaqrM2RY2WYBZRGgOwcu1VwGrmiA5REQBERAEREAREQBERAEREAREQHFEouUQHGEJhC5RAcUCUC5RAcUCUXKIDii5REAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAf/2Q=="/>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Save The Human Project</title>
  <style>
  body {
    color: #000000;
    background-color: #C0C0C0;
    font-family: Arial, sans-serif;
    font-size:14px;
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: none;
  }
  body.blurry {
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: #fff 0px 0px 25px;
  }
  a {
    color: #0188cc;
  }
  .textColumn, .linksColumn {
    padding: 2em;
  }
  .textColumn {
    position: absolute;
    top: 0px;
    right: 50%;
    bottom: 0px;
    left: 0px;
    text-align: right;
    padding-top: 11em;
    background-color: #1BA86D;
    background-image: -moz-radial-gradient(left top, circle, #6AF9BD 0%, #00B386 60%);
    background-image: -webkit-gradient(radial, 0 0, 1, 0 0, 500, from(#6AF9BD), to(#00B386));
  }
  .textColumn p {
    width: 75%;
    float:right;
  }
  .linksColumn {
    position: absolute;
    top:0px;
    right: 0px;
    bottom: 0px;
    left: 50%;
    background-color: #E0E0E0;
  }
  h1 {
    font-size: 500%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  h2 {
    font-size: 200%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  ul {
    padding-left: 1em;
    margin: 0px;
  }
  li {
    margin: 1em 0em;
  }
  </style>
</head>"""

welcome_body = """<body id="sample">
  <div class="textColumn">
  <h1> Stop Human Trafficking</h1>
    <h3> Save The Human Project</h3>
   </div>
  
  <div class="linksColumn"> 
    <h2>Upload Photo</h2>
    <ul>
    <li><a href="http://docs.amazonwebservices.com/elasticbeanstalk/latest/dg/">Upload the photo Here</a></li>
    <br>
      <form action="check" method="post" enctype="multipart/form-data">
        <p></p>
          <font size="4">Select image to upload:</font> <br><br>
        <br>
        <font size="4"> 
          <input type="file" name="fileToUpload" id="fileToUpload" accept="image/*;capture=camera">
          <input type="submit" value="Upload Image" name="submit">
      </form>
    <br>
    </ul>
  </div>
</body>"""

page_end = "</html>"

welcome = web_header + welcome_body + page_end

photo_submission_body_start = "<body><div><p>"

photo_submission_error = "Sorry we cannot process that right now.<br><br>Our monkeys are working it."

photo_submission_body_end = "</p></div></body>"

html_newline = "<br>"

