import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        comment: false
    }
    // getters: {
    //     popupComment(state){
    //         return state.comment
    //     }
    // }
})