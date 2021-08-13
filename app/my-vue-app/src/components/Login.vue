<template height="100%">
    <div id="login">
        <h1> this is login page </h1>
        <input type="text" id="username" v-model="name" placeholder="e-mail"> <br>
        <input type="text" id="password" v-model="pas" placeholder="password"> <br>
        <button type="submit" @click="login">ログイン</button>
    </div>
</template>
<script >
export default{
    name: "Login",
    data() {
        return {
            name: "",
            password: "",
        }
    },
    methods: {
        login: function(){
            const valid = this.valid()
            if (!valid) {
                return 
            }
            alert("成功")
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