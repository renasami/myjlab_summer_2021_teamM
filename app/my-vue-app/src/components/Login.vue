<template>
    <div id="login">
    <div class="login_inner">
        <!-- <img id='logo' alt="VG logo" src="./img/vglogo-white.svg"><br> -->
        <h1> Login Page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="password" id="password" v-model="password" placeholder="password"> <br>
        <button type="submit" @click="firebaseLogin">ログイン</button><br>
        <router-link class='rgster' to="/register">ユーザ登録はこちらから</router-link>
    </div>
    </div>
</template>
<script >
//axios.defaults.withCredentials = true;
import store from "../store"
import { signInWithEmailAndPassword } from "firebase/auth";
import {auth} from "../firebase"


export default{
    name: "Login",
    data() {
        return {
            name: "",
            password: "",
            dialog: false,
        }
    },
    methods: {
        firebaseLogin: function() {
            signInWithEmailAndPassword(auth,this.name,this.password)
            .then(result => {
                store.commit("setUserId",result._tokenResponse.localId)
                store.commit("setIsLogin",true)
                this.$router.push("/home")
                location.reload()
            })
            .catch((w)=>{
                console.log(w)
                store.commit("setUserId","")
                store.commit("setIsLogin",false)

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
    mounted: function() {
        store.commit("setIsLogin",false)
        console.log(store.state)
    }

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