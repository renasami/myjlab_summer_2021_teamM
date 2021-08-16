<template>
    <div>
        <h1> you can test api here </h1>
        <h2> post method</h2>
        <hr/>
        <div id="post-method">
            <lavel>endpoint</lavel>
            <input type="text" v-model="endpoint"><br/>
            <div>
                <button @click="createNewDataFrom" >data追加</button>
                <ul >
                    <li v-for="(form,index) in forms" :key="index">
                        <lavel>key</lavel>
                        <input type="text" v-model="keys[index]">
                        <lavel>value</lavel>
                        <input type="text"  v-model="values[index]">
                    </li>
                </ul>
            </div>
            <button @click="submit(endpoint)">Submit</button>
        </div>
        <hr/>
        <br>
        <h2> get method</h2>
        <hr/>
    </div>
</template>
<script>
export default {
    name: "api-test",
    data() {
        return {
            post: "",
            endpoint: "",
            keys: [],
            values: [],
            forms: [],
            postJson: {},
        }
    },
    methods:{
        createJSON(keys,values,forms){
            keyCount = 0
            keys.forEach(ke => {
                if (!ke) keyCount++;
            })
            if(keyCount == 0){
                alert("今回は配列を送信します。")
            }
            if(keyCount != keys.length){
                alert("keyに抜けがあります")
            }
        },
        submit(endpoint){
            if(!endpoint){
                alert("エンドポイント入力しろハゲ")
            }
            createJSON(this.keys,this.values,this.forms)
            console.log(endpoint)
        },
        createNewDataFrom(){
            this.forms.push("")
            this.keys.push("")
            this.values.push("")
            console.log(this.keys,this.values)
        }
    }
}
</script>
<style >
#post-method{
    margin: 25px;
}
</style>
