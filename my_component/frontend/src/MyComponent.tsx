import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
  ReactElement,
} from "react"

import Cropper from "react-easy-crop"

function MyComponent({ args, disabled, theme }: ComponentProps): ReactElement {
  // Extract custom arguments passed from Python
  const { image, aspect_ratio } = args

  useEffect(() => {
    Streamlit.setFrameHeight()
 
  }, [theme])

  const [crop, setCrop] = useState({ x: 0, y: 0 })
  const [zoom, setZoom] = useState(1)

  const onCropComplete = useCallback((croppedArea: any, croppedAreaPixels: any) => {
    Streamlit.setComponentValue(croppedAreaPixels)
    Streamlit.setFrameHeight()
 
  }, [])

  return (
    <div style={{ height: 400, width: '100%' }}>
      <Cropper
      image={image}
      crop={crop}
      zoom={zoom}
      aspect={aspect_ratio}
      onCropChange={setCrop}
      onCropComplete={onCropComplete}
      onZoomChange={setZoom}
    />

    </div>
  )
}
export default withStreamlitConnection(MyComponent)
