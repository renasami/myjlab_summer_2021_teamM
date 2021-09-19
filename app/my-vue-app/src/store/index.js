import Vuex from 'vuex'
import Vue from 'vue'
import createPersistedState from "vuex-persistedstate";


Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      user:'',
      isLogin: false
    },
    mutations: {
        setUsername (state, input) {
          state.user = input
        },
        setIsLogin (state, input) {
            state.isLogin = input
        }
    },
    plugins: [createPersistedState({storage: window.sessionStorage})]
  })

export default store