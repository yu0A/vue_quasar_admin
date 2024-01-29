const routes = [
  //首页
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "默认分组",
    caption: "默认分组",
    icon: "fas fa-folder-open",
    color: "lime-8",
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
    ],
  },
  //输入框
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "输入框",
    caption: "输入框",
    icon: "fas fa-folder-open",
    color: "red-6",
    children: [
      //input
      {
        path: "/input",
        component: () => import("src/pages/input/input.vue"),
        label: "Input",
        icon: "mail",
        color: "teal",
        children: [],
      },
      //inputJiaoYan
      {
        path: "/inputJiaoYan",
        component: () => import("src/pages/input/inputJiaoYan.vue"),
        label: "Input校验",
        icon: "mail",
        color: "cyan",
        children: [],
      },
    ],
  },
  //表格
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "表格",
    caption: "表格",
    icon: "fas fa-folder-open",
    color: "deep-orange-5",
    children: [
      //table
      {
        path: "/table",
        component: () => import("src/pages/table/table.vue"),
        label: "Table",
        icon: "mail",
        color: "red",
        children: [],
      },
      //tableXingNeng
      {
        path: "/tableXingNeng",
        component: () => import("src/pages/table/tableXingNeng.vue"),
        label: "提升表格性能",
        icon: "mail",
        color: "green-8",
        children: [],
      },
      //markupTable
      {
        path: "/markupTable",
        component: () => import("src/pages/table/markupTable.vue"),
        label: "将任意数据放在表格中",
        icon: "mail",
        color: "blue-8",
        children: [],
      },
      //tableShuRuKuang
      {
        path: "/tableShuRuKuang",
        component: () => import("src/pages/table/tableShuRuKuang.vue"),
        label: "在表格中放置输入框",
        icon: "mail",
        color: "purple-3",
        children: [],
      },
      //tableDuoXuan
      {
        path: "/tableDuoXuan",
        component: () => import("src/pages/table/tableDuoXuan.vue"),
        label: "表格多选",
        icon: "mail",
        color: "teal-8",
        children: [],
      },
      //tableZhanKai
      {
        path: "/tableZhanKai",
        component: () => import("src/pages/table/tableZhanKai.vue"),
        label: "表格展开",
        icon: "mail",
        color: "orange-8",
        children: [],
      },
    ],
  },
  //Python
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "Python",
    caption: "Python",
    icon: "fas fa-folder-open",
    color: "blue-6",
    children: [
      //python
      {
        path: "/python",
        component: () => import("src/pages/python/python.vue"),
        label: "Python",
        icon: "mail",
        color: "yellow",
        children: [],
      },
      //pythonDaTi
      {
        path: "/pythonDaTi",
        component: () => import("src/pages/python/pythonDaTi.vue"),
        label: "Python答题页面",
        icon: "mail",
        color: "accent",
        children: [],
      },
      //pythonDuQuBenDiJiaoBen
      {
        path: "/pythonDuQuBenDiJiaoBen",
        component: () => import("src/pages/python/pythonDuQuBenDiJiaoBen.vue"),
        label: "Python读取本地脚本",
        icon: "mail",
        color: "primary",
        children: [],
      },
      //pythonMianXiangDuiXiangBianCheng
      {
        path: "/pythonMianXiangDuiXiangBianCheng",
        component: () => import("src/pages/python/pythonMianXiangDuiXiangBianCheng.vue"),
        label: "Python面向对象编程",
        icon: "mail",
        color: "secondary",
        children: [],
      },
      //pythonWangLuoDaoRu
      {
        path: "/pythonWangLuoDaoRu",
        component: () => import("src/pages/python/pythonWangLuoDaoRu.vue"),
        label: "Python网络导入",
        icon: "mail",
        color: "red",
        children: [],
      },
    ],
  },
  //NumPy
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "NumPy",
    caption: "NumPy",
    icon: "fas fa-folder-open",
    color: "pink-4",
    children: [
      //numpy
      {
        path: "/numpy",
        component: () => import("src/pages/numpy/numpy.vue"),
        label: "NumPy",
        icon: "mail",
        color: "pink-4",
        children: [],
      },
    ],
  },
  //Matplotlib
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "Matplotlib",
    caption: "Matplotlib",
    icon: "fas fa-folder-open",
    color: "green-4",
    children: [
      //matplotlib
      {
        path: "/matplotlib",
        component: () => import("src/pages/matplotlib/matplotlib.vue"),
        label: "Matplotlib",
        icon: "mail",
        color: "green-4",
        children: [],
      },
      //huizhizitu
      {
        path: "/huizhizitu",
        component: () => import("src/pages/matplotlib/huiZhiZiTu.vue"),
        label: "绘制子图",
        icon: "mail",
        color: "light-green-4",
        children: [],
      },
    ],
  },
  //bcrypt
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "bcrypt",
    caption: "bcrypt",
    icon: "fas fa-folder-open",
    color: "green-4",
    children: [
      //bcrypt
      {
        path: "/bcrypt",
        component: () => import("src/pages/bcrypt/bcrypt.vue"),
        label: "bcrypt",
        icon: "mail",
        color: "green-4",
        children: [],
      },
    ],
  },
  //bitarray
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "bitarray",
    caption: "bitarray",
    icon: "fas fa-folder-open",
    color: "green-4",
    children: [
      //bitarray
      {
        path: "/bitarray",
        component: () => import("src/pages/bitarray/bitarray.vue"),
        label: "bitarray",
        icon: "mail",
        color: "green-4",
        children: [],
      },
    ],
  },
  //bitstring
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    label: "bitstring",
    caption: "bitstring",
    icon: "fas fa-folder-open",
    color: "green-4",
    children: [
      //bitstring
      {
        path: "/bitstring",
        component: () => import("src/pages/bitstring/b.vue"),
        label: "bitstring",
        icon: "mail",
        color: "green-4",
        children: [],
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  // {
  //   label: "404",
  //   path: "/:catchAll(.*)*",
  //   component: () => import("pages/ErrorNotFound.vue"),
  // },
];

export default routes;
