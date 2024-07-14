import React, { useRef, useEffect } from 'react'
import * as monaco from 'monaco-editor'

export const Editor: React.FC = () => {
  const divEl = useRef<HTMLDivElement>(null)
  let editor: monaco.editor.IStandaloneCodeEditor
  useEffect(() => {
    if (divEl.current) {
      editor = monaco.editor.create(divEl.current, {
        value: JSON.stringify({ hello: 123 }, null, 2),
        language: 'json',
      })
    }
    return () => {
      editor.dispose()
    }
  }, [])
  return <div className="Editor" ref={divEl}></div>
}
