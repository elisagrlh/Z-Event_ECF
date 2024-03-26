const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: 'http://localhost:8080',
  outputDir: '../business/static/business/dist/',
  indexPath: '../business/templates/business/index.html'
})
