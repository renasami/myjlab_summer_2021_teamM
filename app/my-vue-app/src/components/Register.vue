<template>
    <div id="register" >
    <div class="register_inner">
        <h1> Register Page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="password" id="password" v-model="password" placeholder="password"> <br>
        <button type="submit" @click="registerFirebase">登録</button><br>
        <router-link class='rgster' to="/login">ログインはこちらから</router-link>

    </div>
    </div>
</template>
<script>
import axios from "axios"
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

let cookies = document.cookie; //全てのcookieを取り出して
let cookiesArray = cookies.split(';'); // ;で分割し配列に

for(var c of cookiesArray){ //一つ一つ取り出して
    var cArray = c.split('='); //さらに=で分割して配列に
    if( cArray[0] == ' isLogin'){ // 取り出したいkeyと合致したら
        if(cArray[1] == "true" & location.pathname == "/register") location.href = "/home"  // [key,value] 
    }
}
export default {
    name: 'Register',
    data() {
        return {
            name: "",
            password: "",
            auth: getAuth(),
        }
    },
    methods: {
        register: async function(){
            const valid = this.valid()
            if (!valid) {
                return 
            }
            // sha256.update(this.password)
            // const hashedPassword = sha256.digest("hex")
            await axios.post("http://0.0.0.0:8000/register/",{mail:this.name,password:this.password}).then(result => {
                console.log(result)
            }).catch(err => {
                console.log(err)
                alert("そのメールアドレスは使用されています。")
            })
            this.$router.push("/home")
        },
        registerFirebase: function(){
            console.log("hello")
            const valid = this.valid();
            if(!valid) return
            createUserWithEmailAndPassword(this.auth, this.name, this.password)
            .then(result => {
                alert("sucsecc")
                console.log(result)
            })
            .catch(e=>{
                console.log(e)
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
#register {
    position:relative;
    width: 100%;
    height: 100vh;
    /* background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab); */
     background: linear-gradient(-45deg, #1c304b, #6da7c9);
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

.register_inner {
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
    text-align: left;
    border: none;
    background-color: rgba(255, 255, 255, 0.2);
    margin-bottom: 15px;
    border-radius: 3px;
    padding-left: 10px;
    font-size: 0.9em;
}

::placeholder {
  color: white;
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