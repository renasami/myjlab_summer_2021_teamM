<template>
    <div id="register" >
        <h1> this is register page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="text" id="password" v-model="password" placeholder="password"> <br>
        <button type="submit" @click="register">登録</button>
    </div>
</template>
<script>
import axios from "axios"
// import crypto from "crypto"
// const sha256 = crypto.createHash('sha256');
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
<style >

</style>