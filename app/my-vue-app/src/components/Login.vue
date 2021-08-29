<template>
    <div id="login">
    <div class="login_inner">
        <!-- <img id='logo' alt="VG logo" src="./img/vglogo-white.svg"><br> -->
        <h1> Login Page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="password" id="password" v-model="password" placeholder="password"> <br>
        <button type="submit" @click="login">ログイン</button><br>
        <a class='rgster' href="/register">ユーザ登録はこちらから</a>
    </div>
    </div>
</template>
<script >
//axios.defaults.withCredentials = true;
import axios from "axios"
//import crypto from "crypto"
//const sha256 = crypto.createHash('sha256');
let cookies = document.cookie; //全てのcookieを取り出して
let cookiesArray = cookies.split(';'); // ;で分割し配列に

for(var c of cookiesArray){ //一つ一つ取り出して
    var cArray = c.split('='); //さらに=で分割して配列に
    if( cArray[0] == ' isLogin'){ // 取り出したいkeyと合致したら
        if(cArray[1] == "true" & location.pathname == "/login") location.href = "/home"  // [key,value] 
    }
}
export default{
    name: "Login",
    data() {
        return {
            name: "kaisei@gmail.com",
            password: "kaiseiota",
            dialog: false,
        }
    },
    methods: {
        login: function(){
            const valid = this.valid()
            if (!valid) {
                return 
            }
            // sha256.update(this.password)
            // const hashedPassword = sha256.digest("hex")
            axios.post('http://0.0.0.0:8000/users/login/',{mail:this.name,password:this.password}).then(result => {
                    if(!result.data[0]){
                        alert('ユーザー名、もしくはパスワードが間違っています。')
                        return 
                    }
                    console.log(result.data)
                    document.cookie = "isLogin=; expires=0";
                    document.cookie = "username=; expires=0";
                    document.cookie = "userid=; expires=0";
                    document.cookie = `isLogin=${result.data[0]}`;
                    document.cookie = `username=${this.name.substring(0, this.name.indexOf("@"))}`;
                    document.cookie = `userid=${result.data[1]["user_id"]}`;
                    location.href="/home"
                })
        },
        valid() {
            if (/\p{Emoji_Modifier_Base}\p{Emoji_Modifier}?|\p{Emoji_Presentation}|\p{Emoji}\uFE0F/gu.test(this.name)) {
                alert("絵文字はだめです")
                return false
            }
            if(!this.name.includes("@")){
                alert("e-mailアドレスを入力してください")
                return false
            }
            if(/\p{Emoji_Modifier_Base}\p{Emoji_Modifier}?|\p{Emoji_Presentation}|\p{Emoji}\uFE0F/gu.test(this.password)){
                alert("パスワードは半角英数字です。")
                return false
            }
            if(this.password.length < 8 || this.password.length > 16){
                alert("パスワードは8文字以上16文字以下で入力してください。")
                return false
            }
            return true
        }
    },

}

</script>


<style scoped>
/* lang="stylus" */

#login {
    position:relative;
    width: 100%;
    height: 100vh;
    /* background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab); */
     background: linear-gradient(-45deg, #184e68, #57ca85);
    background-size: 200% 200%;
    animation: gradient 8s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.login_inner {
    position:absolute;
  top: 50%;
  left: 50%;
  transform: translateY(-50%) translateX(-50%);
    -webkit-transform: translateY(-50%) translateX(-50%);
    padding-bottom:50px;
}

h1 {
    color: white;
    margin-bottom: 20px;
    font-weight: bold;
    text-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
}

input {
    width:300px;
    height:55px;
    color: white;
    text-align: left;
    border: none;
    background-color: rgba(255, 255, 255, 0.2);
    margin-bottom: 15px;
    border-radius: 3px;
    padding-left: 10px;
    font-size: 0.9em;
}

button {
    width:310px;
    height: 53px;
    color: rgba(255, 255, 255, 1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: transparent;
    border-radius: 3px;
    margin-bottom: 10px;
    font-size: 0.9em;
}

button:hover, .rgster:hover {
    color: rgba(255, 255, 255, 0.5);
}

.rgster {
    font-size: 0.75em;
    color: white;
    text-decoration: none;
}

</style>