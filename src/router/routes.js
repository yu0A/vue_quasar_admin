const routes = [
  //首页
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "MainLayout",
    icon: "mail",
    color: "purple",
    children: [
      //page1
      {
        path: "/page1",
        component: () => import("pages/basic/page1.vue"),
        label: "Page One",
        icon: "mail",
        color: "orange",
        children: [],
      },
      //input
      {
        path: "/input",
        component: () => import("pages/basic/input.vue"),
        label: "Input",
        icon: "mail",
        color: "teal",
        children: [],
      },
      //table
      {
        path: "/table",
        component: () => import("pages/basic/table.vue"),
        label: "Table",
        icon: "mail",
        color: "red",
        children: [],
      },
      //python
      {
        path: "/python",
        component: () => import("pages/basic/python.vue"),
        label: "Python",
        icon: "mail",
        color: "yellow",
        children: [],
      },
      //pythonDaTi
      {
        path: "/pythonDaTi",
        component: () => import("pages/basic/pythonDaTi.vue"),
        label: "Python答题页面",
        icon: "mail",
        color: "accent",
        children: [],
      },
      //pythonDuQuBenDiJiaoBen
      {
        path: "/pythonDuQuBenDiJiaoBen",
        component: () => import("pages/basic/pythonDuQuBenDiJiaoBen.vue"),
        label: "Python读取本地脚本",
        icon: "mail",
        color: "primary",
        children: [],
      },
      //pythonMianXiangDuiXiangBianCheng
      {
        path: "/pythonMianXiangDuiXiangBianCheng",
        component: () => import("pages/basic/pythonMianXiangDuiXiangBianCheng.vue"),
        label: "Python面向对象编程",
        icon: "mail",
        color: "secondary",
        children: [],
      },
      //pythonWangLuoDaoRu
      {
        path: "/pythonWangLuoDaoRu",
        component: () => import("pages/basic/pythonWangLuoDaoRu.vue"),
        label: "Python网络导入",
        icon: "mail",
        color: "red",
        children: [],
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    label: "404",
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
