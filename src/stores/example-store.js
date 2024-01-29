import { defineStore, acceptHMRUpdate } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({
    footerNote: "欢迎使用",
    pyodide: null,
    globalLoading: false,
  }),
  getters: {
    getFooterNote: (footerNote) => footerNote,
  },
  actions: {
    setFooterNote(footerNote) {
      this.footerNote = footerNote;
    },
    setPyodide(pyodide) {
      this.pyodide = pyodide;
    },
    setGlobalLoading(globalLoading) {
      this.globalLoading = globalLoading;
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCounterStore, import.meta.hot))
}