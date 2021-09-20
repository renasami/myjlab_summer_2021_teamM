import Vuex from 'vuex'
import Vue from 'vue'
import createPersistedState from "vuex-persistedstate";


Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      user:'',
      userId:'',
      likedList:[],
      isLogin: false,
      imgsrc:"./img/Profile.png"
    },
    mutations: {
        setState(state,constructor,input){
            state[constructor] = input;
        },
        setUsername (state, input) {
          state.user = input
        },
        setUserId (state, input) {
            state.userId = input
        },
        setIsLogin (state, input) {
            state.isLogin = input
        },
        settImageSrc (state, input) {
            state.imgsrc = input
        }
    },
    plugins: [createPersistedState({storage: window.sessionStorage})]
  })

export default store