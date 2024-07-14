import cfg from '../../../config.json'

// @ts-ignore
self.MonacoEnvironment = {
  getWorkerUrl: function (_moduleId: any, label: string) {
    if (label === 'json') {
      return `${cfg.web}/json.worker.js`
    }
    return `${cfg.web}/editor.worker.js`
  },
}
