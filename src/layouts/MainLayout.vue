<template>
  <q-layout view="lHh lpR fFf">
    <q-header reveal elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          Title
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" behavior="desktop" bordered>
      <q-tree :nodes="routes" node-key="label" children-key="children" label-key="label" default-expand-all fit>
        <template v-slot:default-header="prop">
          <q-list fit style="min-width: 100px; width: 100%" :bordered="true" class="q-my-none rounded-borders">
            <q-item clickable v-ripple @click="routesTo(prop.node)">
              <q-item-section>{{ prop.node.label }}</q-item-section>
              <q-item-section avatar>
                <q-icon :color="prop.node.color" :name="prop.node.icon" />
              </q-item-section>
            </q-item>
          </q-list>
        </template>
      </q-tree>
    </q-drawer>

    <q-drawer v-model="rightDrawerOpen" side="right" overlay behavior="desktop" bordered>
      <!-- drawer content -->
      <!-- drawer content -->
      <q-tabs vertical inline-label>
        <div align="left" v-for="(v, k) in routes" :key="k">
          <q-route-tab :to="v.path" :label="v.label" :icon="v.icon" :class="v.color" />
        </div>
      </q-tabs>
    </q-drawer>

    <q-page-container>
      <q-inner-loading :showing="visible" style="position: absolute; z-index: 1000000">
        <q-spinner-gears size="50px" color="primary" />
      </q-inner-loading>
      <router-view />
    </q-page-container>

    <q-footer reveal elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <div>{{ store.footerNote }}</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
import { ref, onMounted, computed, getCurrentInstance, onBeforeMount } from "vue";
import routes from "src/router/routes";
import { useRouter } from "vue-router";
import { useCounterStore } from "src/stores/example-store";
import { loadPyodide } from "src/js/pyodide/pyodide.mjs";

export default {
  setup() {
    //实例
    let instance = getCurrentInstance();
    //全局变量存储
    const store = useCounterStore();
    const leftDrawerOpen = ref(false);
    const rightDrawerOpen = ref(false);
    let router = useRouter();
    // 加载Python环境
    let visible = computed(() => store.globalLoading);
    let pyodide = ref(null);
    let initPyodide = async () => {
      pyodide = await loadPyodide();
      Promise.resolve().then(res => {
        store.setPyodide(pyodide);
        setTimeout(() => {
          store.setGlobalLoading(false);
        }, 2000);
      });
    };

    onMounted(async () => {
      store.setGlobalLoading(true);
      initPyodide();
    });

    return {
      visible,
      store,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },

      rightDrawerOpen,
      toggleRightDrawer() {
        rightDrawerOpen.value = !rightDrawerOpen.value;
      },
      routes,
      routesTo(node) {
        router.push(node.path);
      },
    };
  },
};
</script>
