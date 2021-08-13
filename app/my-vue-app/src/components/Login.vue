<template height="100%">
    <div id="login">
        <h1> this is login page </h1>
        <label for="username">fas</label>
        <input type="text" id="username" v-model="name"> <br>
        <label for="password">fas</label>
        <input type="text" id="password" v-model="pas"> <br>
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

        }
    }
}

</script>
<style lang="stylus" scoped>

</style>