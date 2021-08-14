<template>
<div class="card">
    <div v-for="(items, index) in groupedArray" :key="index">
        <li class='cards' v-for="(item, index) in items" :key="index">
        <div class='cards_inner'>
        <div class='upper_video'></div>
        <div class='lower_text'>{{ item }}</div>
        </div>
        </li>
    </div>

</div>
</template>

<script>
export default {

     name: 'Card',
   data: function () {
     return {
        list: [
            "Video1",
            "Video2",
            "Video3",
            "Video4",
            "Video5",
            "Video6",
            "Video7"
        ]
     }
   },
computed: {
  groupedArray() {
    const base = this.list.length
    const split_cnt = 3       // 何個ずつに分割するか
    const grouped_list = []
    for (let i=0; i<Math.ceil(base/split_cnt); i++) {
      let multiple_cnt = i * split_cnt  // 3の倍数
      // (i * 3)番目から(i * 3 + 3)番目まで取得
      let result = this.list.slice(multiple_cnt, multiple_cnt + split_cnt) 
      grouped_list.push(result)
    }
    return grouped_list
    // [
    //   ["AMETHYST", "BLUE-SAPPHIRE", "CITRIN"],
    //   ["DIAMOND", "EMERALD", "FIRE-OPAL"], ...
    // ]
  }
}

}
</script>

<style scoped>
.card {
  width:82%;
  position: absolute;
  right: 0;
}

.cards {
  width:300px;
  height:250px;
  margin: 20px 20px;
  display: inline-block;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
}

.cards_inner {
  margin: 0 auto;
  width:95%;
  height:95%;
}

.upper_video {
  width:100%;
  height:60%;
  background-color:#F7F7F7;
  box-shadow: 0px 2px 6px 0 rgba(0,0,0,0.2);
  border-radius: 3px;
}

.loxer_text {
  width:100%;
  height:40%;
}
</style>