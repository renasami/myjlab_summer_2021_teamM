<template height="100%">
    <div id="login">
        <h1> this is login page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="text" id="password" v-model="password" placeholder="password"> <br>
        <button type="submit" @click="login">ログイン</button>
    </div>
</template>
<script >

//axios.defaults.withCredentials = true;
export default{
    name: "Login",
    data() {
        return {
            name: "kaiseiota0620@gmail.com",
            password: "peter555",
        }
    },
    methods: {
        login: function(){
            const valid = this.valid()
            if (!valid) {
                return 
            }
            this.axios.get("http://0.0.0.0:8000").then(res => console.log(res))
            this.axios.post("http://0.0.0.0:8000/login")
                .then(result => {
                    if(!result){
                        
                    }
                    this.$router.push("/home")
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
<style lang="stylus" scoped>

</style>