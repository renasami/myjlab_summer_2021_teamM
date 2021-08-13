<template height="100%">
    <div id="login">
        <h1> this is login page </h1>
        <input type="text" id="username" v-model="name" placeholder="ユーザ名orE-mail"> <br>
        <input type="text" id="password" v-model="pas" placeholder="password"> <br>
        <button type="submit">ログイン</button>
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
        login() {
        
        },
        valid() {
            console.log(name)
        }
    }
}

</script>
<style lang="stylus" scoped>

</style>