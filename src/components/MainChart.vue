<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart, PieChart } from 'echarts/charts'
import { DatasetComponent, GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { useAppStore } from '../stores/app'

const appStore = useAppStore()

use([
  CanvasRenderer,
  LineChart,
  PieChart,
  LegendComponent,
  TooltipComponent,
  DatasetComponent,
  GridComponent,
])

provide(THEME_KEY, 'default')

const option = reactive({
  title: {
    text: 'Total de Recursos Empenhados e Liquidados',
  },
  tooltip: {
    trigger: 'axis',
    showContent: false,
  },
  legend: {
    data: ['Liquidado', 'Empenhado'],
    left: '1%',
  },
  grid: {
    left: '1%',
    right: '22.5%',
    bottom: '3%',
    containLabel: true,
  },
  toolbox: {
    feature: {
      saveAsImage: {},
    },
  },
  dataset: {
    source: [
      ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
      ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
      ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
      ['Cheese Cocoa', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
      ['Walnut Brownie', 25.2, 37.1, 41.2, 18, 33.9, 49.1],
    ],
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    axisLabel: {
      margin: 20,
    },
  },
  yAxis: {
    type: 'value',
    gridIndex: 0,
  },
  series: [
    {
      name: 'Liquidado',
      type: 'line',
      stack: 'Liquidado',
      smooth: true,
      seriesLayoutBy: 'row',
      emphasis: { focus: 'series' },
      data: [120, 132, 101, 134, 90, 230], // Substitua com seus dados
    },
    {
      name: 'Empenhado',
      type: 'line',
      stack: 'Empenhado',
      smooth: true,
      seriesLayoutBy: 'row',
      emphasis: { focus: 'series' },
      data: [220, 182, 191, 234, 290, 330], // Substitua com seus dados
    },
    {
      type: 'pie',
      id: 'pie',
      radius: '50%',
      center: ['90%', '50%'],
      emphasis: {
        focus: 'self',
        label: {
          show: true,
        },
      },
      label: {
        show: false,
        formatter: '{d}%',
        fontSize: 15,
        color: appStore.isDark ? '#fff' : '#000',
        fontWeight: 'bold',
        position: 'center',
      },
      encode: {
        itemName: 'product',
        value: '2012',
        tooltip: '2012',
      },
      data: [
        {
          value: 335, // Substitua com sua variável settled
          name: 'Liquidado',
        },
        {
          value: 310, // Substitua com sua variável committed
          name: 'Empenhado',
        },
      ],
    },
  ],
})

const onEvents = {
  updateAxisPointer: event => {
    const xAxisInfo = event.axesInfo[0]
    if (xAxisInfo) {
      const dimension = xAxisInfo.value + 1
      option.series.forEach(serie => {
        if (serie.id === 'pie') {
          serie.label.formatter = `{b}: {@[${dimension}]} ({d}%)`
          serie.encode.value = dimension
          serie.encode.tooltip = dimension
        }
      })
    }
  },
}
</script>

<template>
  <div class="chart-dataset ma-16">
    {{appStore.isDark}}
    <TitleSection title="Total de Recursos Empenhados e Liquidados" />
    <v-chart class="chart" :option="option" @events="onEvents" />
  </div>
</template>

<style lang="css" scoped>
  .chart-dataset {
    height: 400px;
  }
</style>
