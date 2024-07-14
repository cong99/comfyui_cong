import './index.css'
// import '@fontsource/roboto/300.css';
// import '@fontsource/roboto/400.css';
// import '@fontsource/roboto/500.css';
// import '@fontsource/roboto/700.css';

import './plugins/monaco'
import React from 'react'
import ReactDOM from 'react-dom'
import { Editor } from './components/Editor'
import ButtonEx from './components/ButtonEx'
import DataGrid from './components/DataGrid'

export function createTable($el: Element) {
  ReactDOM.render(
    <React.StrictMode>
      <ButtonEx />
      <Editor />
      <DataGrid />
    </React.StrictMode>,
    $el
  )
}
