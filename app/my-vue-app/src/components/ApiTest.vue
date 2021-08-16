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
        <div>
            <h2> get method</h2>
            <button @click="getData">Get</button>
        </div>
        <hr/>
        <p>
            エンドポイントを'/name'の形式で入力するとそこに対するget/postの処理が行えます。<br/>
            postは配列/jsonのみ対応。keyを全て空白にすることで送る配列で送れます。<br/>
            jsonのvalueを配列にしたいときは手打ちで。あとで配列もひとつずつ入力できるようにします。
        </p>
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
            postArry:[]
        }
    },
    methods:{
        createJSON(keys,values,forms){
            let keyCount = 0
            keys.forEach(ke => {
                if (ke) {
                    keyCount++
                    console.log(ke)
                }
            })
            if(keyCount == 0){
                alert("今回は配列を送信します。")
                this.postArry = values
                this.axios.post("http://0.0.0.0:8080"+this.endpoint,this.postArry)
                .then(response => alert(response.data)).catch(error =>alert(error.message))
            }
            if(keyCount != keys.length){
                alert("keyに抜けがあります")
                return 
            }
            forms.forEach(index => {
                this.postJson[keys[index]] = values[index]
            })
            console.log(this.postJson)
            this.axios.post("http://0.0.0.0:8080"+this.endpoint,this.postJson)
                .then(response => alert(response.data)).catch(error =>alert(error.message))
        },
        submit(endpoint){
            if(!endpoint){
                alert("エンドポイント入力しろハゲ")
            }
            this.createJSON(this.keys,this.values,this.forms)
            console.log(endpoint)
        },
        createNewDataFrom(){
            this.forms.push(this.forms.length)
            this.keys.push("")
            this.values.push("")
            console.log(this.keys,this.values)
        },
        getData(){
            this.axios.get('http://0.0.0.0:8000'+this.endpoint).then(result => alert(result)).catch(error => alert(error))
        }
    }
}
</script>
<style >
#post-method{
    margin: 25px;
}
</style>
