<template lang="pug">
  .chart-container
    canvas
</template>

<style lang="stylus" scoped>
  .chart-container
      display : block
      width   : 100%
      height  : 380px
      padding : 0
      margin  : 1em auto
</style>

<script>
  import Chart from 'chart.js'
  import options from './chart.options.yml'
  export default {
    props: {
      labels: {
        required: true,
      },
      probabilities: {
        required: true,
      },
    },
    data: () => ({
      chart: null,
    }),
    watch: {
      probabilities(){
        const data = !this.probabilities ? [] : this.probabilities
        this.chart.data.datasets[0].data = data
        this.chart.update()
      },
    },
    mounted(){
      this._canvas = this.$el.querySelector('canvas')
      this.chart = new Chart(this._canvas, {
        type: 'bar',
        data: {
          labels: this.labels,
          datasets: [{
            label: 'Probabilities',
            data: this.probabilities,
          }]
        },
        options,
      })
    },
  }
</script>
