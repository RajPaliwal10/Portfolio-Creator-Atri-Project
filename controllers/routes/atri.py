import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"Flex1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div6":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex13":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex16":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex17":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex18":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex19":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex21":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex22":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex7":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex8":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex23":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex25":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex26":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex9":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex32":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex40":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex41":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex45":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex46":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex47":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex48":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex33":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex35":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex36":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex37":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex38":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex39":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex55":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex56":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex61":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex57":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex58":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex64":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex67":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex68":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex85":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex86":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex87":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex62":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex71":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex88":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex93":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex94":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex100":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex74":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex76":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex79":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex83":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex84":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex89":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex90":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex91":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex60":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex101":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex102":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex104":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex105":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex106":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex107":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex103":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex108":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex113":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex109":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex114":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex115":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex116":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex110":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex117":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex118":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex119":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex111":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex120":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex121":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex122":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex112":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex123":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex124":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex125":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex129":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex128":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex132":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex133":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex130":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex134":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex135":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex137":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex138":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex136":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex139":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex140":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex143":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex144":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex146":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex158":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex164":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex165":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex159":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex166":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex167":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex147":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex154":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex155":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex148":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex160":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex173":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex171":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex172":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex149":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex162":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex176":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex174":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex175":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex145":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex152":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex204":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex202":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex198":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex199":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex203":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex200":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex201":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex153":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex156":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex157":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex232":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex230":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex226":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex227":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex231":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex228":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex229":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex239":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex237":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex233":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex234":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex238":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex235":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex236":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex240":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex245":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex246":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex249":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex252":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex248":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex244":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex241":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex242":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex243":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex253":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex254":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex255":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex256":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex257":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex278":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex280":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex281":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex258":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex263":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex274":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex279":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex282":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex283":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex296":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex293":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex295":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex294":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex297":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex292":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex291":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"TextBox1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox17":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox20":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox19":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox18":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox22":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox23":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox13":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox14":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Button6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Image1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox29":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox31":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image9":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox33":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox37":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image12":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image10":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox34":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox38":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image13":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image11":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox36":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox39":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image14":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox28":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox48":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Button7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"Image16":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox50":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox51":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox52":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image19":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image17":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox54":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox59":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox53":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox62":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image22":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image18":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox56":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox55":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image21":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox57":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox58":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox46":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox64":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox65":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox66":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image24":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox73":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox74":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox75":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image25":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox77":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox79":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox80":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image26":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox81":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox82":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox83":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image27":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox84":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox85":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox86":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image28":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox87":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox88":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox89":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image29":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox91":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox90":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox93":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image31":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image30":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image33":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image32":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox97":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox96":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox98":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image36":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image34":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox94":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox101":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox102":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image39":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox105":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox108":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox109":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox110":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image40":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Image45":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox121":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox122":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox123":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image35":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox95":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox133":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox134":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox135":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image49":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox136":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox137":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox138":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image50":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox142":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox143":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image51":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox141":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image52":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox139":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox140":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox144":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox145":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox168":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox169":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox162":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox163":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox160":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox161":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox164":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox165":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox176":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox178":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox177":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox181":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox179":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox180":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"]
		self.Div6 = state["Div6"]
		self.Flex13 = state["Flex13"]
		self.Flex16 = state["Flex16"]
		self.Flex17 = state["Flex17"]
		self.Flex18 = state["Flex18"]
		self.Flex19 = state["Flex19"]
		self.Flex21 = state["Flex21"]
		self.Flex22 = state["Flex22"]
		self.Flex7 = state["Flex7"]
		self.Flex8 = state["Flex8"]
		self.Flex23 = state["Flex23"]
		self.Flex25 = state["Flex25"]
		self.Flex26 = state["Flex26"]
		self.Flex9 = state["Flex9"]
		self.Flex32 = state["Flex32"]
		self.Flex40 = state["Flex40"]
		self.Flex41 = state["Flex41"]
		self.Flex45 = state["Flex45"]
		self.Flex46 = state["Flex46"]
		self.Flex47 = state["Flex47"]
		self.Flex48 = state["Flex48"]
		self.Flex33 = state["Flex33"]
		self.Flex35 = state["Flex35"]
		self.Flex36 = state["Flex36"]
		self.Flex37 = state["Flex37"]
		self.Flex38 = state["Flex38"]
		self.Flex39 = state["Flex39"]
		self.Flex55 = state["Flex55"]
		self.Flex56 = state["Flex56"]
		self.Flex61 = state["Flex61"]
		self.Flex57 = state["Flex57"]
		self.Flex58 = state["Flex58"]
		self.Flex64 = state["Flex64"]
		self.Flex67 = state["Flex67"]
		self.Flex68 = state["Flex68"]
		self.Flex85 = state["Flex85"]
		self.Flex86 = state["Flex86"]
		self.Flex87 = state["Flex87"]
		self.Flex62 = state["Flex62"]
		self.Flex71 = state["Flex71"]
		self.Flex88 = state["Flex88"]
		self.Flex93 = state["Flex93"]
		self.Flex94 = state["Flex94"]
		self.Flex100 = state["Flex100"]
		self.Flex74 = state["Flex74"]
		self.Flex76 = state["Flex76"]
		self.Flex79 = state["Flex79"]
		self.Flex83 = state["Flex83"]
		self.Flex84 = state["Flex84"]
		self.Flex89 = state["Flex89"]
		self.Flex90 = state["Flex90"]
		self.Flex91 = state["Flex91"]
		self.Flex60 = state["Flex60"]
		self.Flex101 = state["Flex101"]
		self.Flex102 = state["Flex102"]
		self.Flex104 = state["Flex104"]
		self.Flex105 = state["Flex105"]
		self.Flex106 = state["Flex106"]
		self.Flex107 = state["Flex107"]
		self.Flex103 = state["Flex103"]
		self.Flex108 = state["Flex108"]
		self.Flex113 = state["Flex113"]
		self.Flex109 = state["Flex109"]
		self.Flex114 = state["Flex114"]
		self.Flex115 = state["Flex115"]
		self.Flex116 = state["Flex116"]
		self.Flex110 = state["Flex110"]
		self.Flex117 = state["Flex117"]
		self.Flex118 = state["Flex118"]
		self.Flex119 = state["Flex119"]
		self.Flex111 = state["Flex111"]
		self.Flex120 = state["Flex120"]
		self.Flex121 = state["Flex121"]
		self.Flex122 = state["Flex122"]
		self.Flex112 = state["Flex112"]
		self.Flex123 = state["Flex123"]
		self.Flex124 = state["Flex124"]
		self.Flex125 = state["Flex125"]
		self.Flex129 = state["Flex129"]
		self.Flex128 = state["Flex128"]
		self.Flex132 = state["Flex132"]
		self.Flex133 = state["Flex133"]
		self.Flex130 = state["Flex130"]
		self.Flex134 = state["Flex134"]
		self.Flex135 = state["Flex135"]
		self.Flex137 = state["Flex137"]
		self.Flex138 = state["Flex138"]
		self.Flex136 = state["Flex136"]
		self.Flex139 = state["Flex139"]
		self.Flex140 = state["Flex140"]
		self.Flex143 = state["Flex143"]
		self.Flex144 = state["Flex144"]
		self.Flex146 = state["Flex146"]
		self.Flex158 = state["Flex158"]
		self.Flex164 = state["Flex164"]
		self.Flex165 = state["Flex165"]
		self.Flex159 = state["Flex159"]
		self.Flex166 = state["Flex166"]
		self.Flex167 = state["Flex167"]
		self.Flex147 = state["Flex147"]
		self.Flex154 = state["Flex154"]
		self.Flex155 = state["Flex155"]
		self.Flex148 = state["Flex148"]
		self.Flex160 = state["Flex160"]
		self.Flex173 = state["Flex173"]
		self.Flex171 = state["Flex171"]
		self.Flex172 = state["Flex172"]
		self.Flex149 = state["Flex149"]
		self.Flex162 = state["Flex162"]
		self.Flex176 = state["Flex176"]
		self.Flex174 = state["Flex174"]
		self.Flex175 = state["Flex175"]
		self.Flex145 = state["Flex145"]
		self.Flex152 = state["Flex152"]
		self.Flex204 = state["Flex204"]
		self.Flex202 = state["Flex202"]
		self.Flex198 = state["Flex198"]
		self.Flex199 = state["Flex199"]
		self.Flex203 = state["Flex203"]
		self.Flex200 = state["Flex200"]
		self.Flex201 = state["Flex201"]
		self.Flex153 = state["Flex153"]
		self.Flex156 = state["Flex156"]
		self.Flex157 = state["Flex157"]
		self.Flex232 = state["Flex232"]
		self.Flex230 = state["Flex230"]
		self.Flex226 = state["Flex226"]
		self.Flex227 = state["Flex227"]
		self.Flex231 = state["Flex231"]
		self.Flex228 = state["Flex228"]
		self.Flex229 = state["Flex229"]
		self.Flex239 = state["Flex239"]
		self.Flex237 = state["Flex237"]
		self.Flex233 = state["Flex233"]
		self.Flex234 = state["Flex234"]
		self.Flex238 = state["Flex238"]
		self.Flex235 = state["Flex235"]
		self.Flex236 = state["Flex236"]
		self.Flex240 = state["Flex240"]
		self.Flex245 = state["Flex245"]
		self.Flex246 = state["Flex246"]
		self.Flex249 = state["Flex249"]
		self.Flex252 = state["Flex252"]
		self.Flex248 = state["Flex248"]
		self.Flex244 = state["Flex244"]
		self.Flex241 = state["Flex241"]
		self.Flex242 = state["Flex242"]
		self.Flex243 = state["Flex243"]
		self.Flex253 = state["Flex253"]
		self.Flex254 = state["Flex254"]
		self.Flex255 = state["Flex255"]
		self.Flex256 = state["Flex256"]
		self.Flex257 = state["Flex257"]
		self.Flex278 = state["Flex278"]
		self.Flex280 = state["Flex280"]
		self.Flex281 = state["Flex281"]
		self.Flex258 = state["Flex258"]
		self.Flex263 = state["Flex263"]
		self.Flex274 = state["Flex274"]
		self.Flex279 = state["Flex279"]
		self.Flex282 = state["Flex282"]
		self.Flex283 = state["Flex283"]
		self.Flex296 = state["Flex296"]
		self.Flex293 = state["Flex293"]
		self.Flex295 = state["Flex295"]
		self.Flex294 = state["Flex294"]
		self.Flex297 = state["Flex297"]
		self.Flex292 = state["Flex292"]
		self.Flex291 = state["Flex291"]
		self.TextBox1 = state["TextBox1"]
		self.TextBox17 = state["TextBox17"]
		self.TextBox20 = state["TextBox20"]
		self.TextBox19 = state["TextBox19"]
		self.TextBox18 = state["TextBox18"]
		self.TextBox22 = state["TextBox22"]
		self.Image3 = state["Image3"]
		self.TextBox23 = state["TextBox23"]
		self.TextBox13 = state["TextBox13"]
		self.TextBox14 = state["TextBox14"]
		self.Button4 = state["Button4"]
		self.Button6 = state["Button6"]
		self.Image1 = state["Image1"]
		self.TextBox29 = state["TextBox29"]
		self.TextBox31 = state["TextBox31"]
		self.Image9 = state["Image9"]
		self.TextBox33 = state["TextBox33"]
		self.TextBox37 = state["TextBox37"]
		self.Image12 = state["Image12"]
		self.Image10 = state["Image10"]
		self.TextBox34 = state["TextBox34"]
		self.TextBox38 = state["TextBox38"]
		self.Image13 = state["Image13"]
		self.Image11 = state["Image11"]
		self.TextBox36 = state["TextBox36"]
		self.TextBox39 = state["TextBox39"]
		self.Image14 = state["Image14"]
		self.TextBox28 = state["TextBox28"]
		self.Image5 = state["Image5"]
		self.Image6 = state["Image6"]
		self.Image7 = state["Image7"]
		self.Image8 = state["Image8"]
		self.TextBox48 = state["TextBox48"]
		self.Button7 = state["Button7"]
		self.Image16 = state["Image16"]
		self.TextBox50 = state["TextBox50"]
		self.TextBox51 = state["TextBox51"]
		self.TextBox52 = state["TextBox52"]
		self.Image19 = state["Image19"]
		self.Image17 = state["Image17"]
		self.TextBox54 = state["TextBox54"]
		self.TextBox59 = state["TextBox59"]
		self.TextBox53 = state["TextBox53"]
		self.TextBox62 = state["TextBox62"]
		self.Image22 = state["Image22"]
		self.Image18 = state["Image18"]
		self.TextBox56 = state["TextBox56"]
		self.TextBox55 = state["TextBox55"]
		self.Image21 = state["Image21"]
		self.TextBox57 = state["TextBox57"]
		self.TextBox58 = state["TextBox58"]
		self.TextBox46 = state["TextBox46"]
		self.TextBox64 = state["TextBox64"]
		self.TextBox65 = state["TextBox65"]
		self.TextBox66 = state["TextBox66"]
		self.Image24 = state["Image24"]
		self.TextBox73 = state["TextBox73"]
		self.TextBox74 = state["TextBox74"]
		self.TextBox75 = state["TextBox75"]
		self.Image25 = state["Image25"]
		self.TextBox77 = state["TextBox77"]
		self.TextBox79 = state["TextBox79"]
		self.TextBox80 = state["TextBox80"]
		self.Image26 = state["Image26"]
		self.TextBox81 = state["TextBox81"]
		self.TextBox82 = state["TextBox82"]
		self.TextBox83 = state["TextBox83"]
		self.Image27 = state["Image27"]
		self.TextBox84 = state["TextBox84"]
		self.TextBox85 = state["TextBox85"]
		self.TextBox86 = state["TextBox86"]
		self.Image28 = state["Image28"]
		self.TextBox87 = state["TextBox87"]
		self.TextBox88 = state["TextBox88"]
		self.TextBox89 = state["TextBox89"]
		self.Image29 = state["Image29"]
		self.TextBox91 = state["TextBox91"]
		self.TextBox90 = state["TextBox90"]
		self.TextBox93 = state["TextBox93"]
		self.Image31 = state["Image31"]
		self.Image30 = state["Image30"]
		self.Image33 = state["Image33"]
		self.Image32 = state["Image32"]
		self.TextBox97 = state["TextBox97"]
		self.TextBox96 = state["TextBox96"]
		self.TextBox98 = state["TextBox98"]
		self.Image36 = state["Image36"]
		self.Image34 = state["Image34"]
		self.TextBox94 = state["TextBox94"]
		self.TextBox101 = state["TextBox101"]
		self.TextBox102 = state["TextBox102"]
		self.Image39 = state["Image39"]
		self.TextBox105 = state["TextBox105"]
		self.TextBox108 = state["TextBox108"]
		self.TextBox109 = state["TextBox109"]
		self.TextBox110 = state["TextBox110"]
		self.Image40 = state["Image40"]
		self.Image45 = state["Image45"]
		self.TextBox121 = state["TextBox121"]
		self.TextBox122 = state["TextBox122"]
		self.TextBox123 = state["TextBox123"]
		self.Image35 = state["Image35"]
		self.TextBox95 = state["TextBox95"]
		self.TextBox133 = state["TextBox133"]
		self.TextBox134 = state["TextBox134"]
		self.TextBox135 = state["TextBox135"]
		self.Image49 = state["Image49"]
		self.TextBox136 = state["TextBox136"]
		self.TextBox137 = state["TextBox137"]
		self.TextBox138 = state["TextBox138"]
		self.Image50 = state["Image50"]
		self.TextBox142 = state["TextBox142"]
		self.TextBox143 = state["TextBox143"]
		self.Image51 = state["Image51"]
		self.TextBox141 = state["TextBox141"]
		self.Image52 = state["Image52"]
		self.TextBox139 = state["TextBox139"]
		self.TextBox140 = state["TextBox140"]
		self.TextBox144 = state["TextBox144"]
		self.TextBox145 = state["TextBox145"]
		self.TextBox168 = state["TextBox168"]
		self.TextBox169 = state["TextBox169"]
		self.TextBox162 = state["TextBox162"]
		self.TextBox163 = state["TextBox163"]
		self.TextBox160 = state["TextBox160"]
		self.TextBox161 = state["TextBox161"]
		self.TextBox164 = state["TextBox164"]
		self.TextBox165 = state["TextBox165"]
		self.TextBox176 = state["TextBox176"]
		self.TextBox178 = state["TextBox178"]
		self.TextBox177 = state["TextBox177"]
		self.TextBox181 = state["TextBox181"]
		self.TextBox179 = state["TextBox179"]
		self.TextBox180 = state["TextBox180"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		global default_state
		self._Flex1 = Flex(new_state, default_state["Flex1"])

	@property
	def Div6(self):
		self._getter_access_tracker["Div6"] = {}
		return self._Div6
	@Div6.setter
	def Div6(self, new_state):
		self._setter_access_tracker["Div6"] = {}
		global default_state
		self._Div6 = Div(new_state, default_state["Div6"])

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		global default_state
		self._Flex13 = Flex(new_state, default_state["Flex13"])

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		global default_state
		self._Flex16 = Flex(new_state, default_state["Flex16"])

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		global default_state
		self._Flex17 = Flex(new_state, default_state["Flex17"])

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		global default_state
		self._Flex18 = Flex(new_state, default_state["Flex18"])

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		global default_state
		self._Flex19 = Flex(new_state, default_state["Flex19"])

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		global default_state
		self._Flex21 = Flex(new_state, default_state["Flex21"])

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		global default_state
		self._Flex22 = Flex(new_state, default_state["Flex22"])

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		global default_state
		self._Flex7 = Flex(new_state, default_state["Flex7"])

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		global default_state
		self._Flex8 = Flex(new_state, default_state["Flex8"])

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		global default_state
		self._Flex23 = Flex(new_state, default_state["Flex23"])

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		global default_state
		self._Flex25 = Flex(new_state, default_state["Flex25"])

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		global default_state
		self._Flex26 = Flex(new_state, default_state["Flex26"])

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		global default_state
		self._Flex9 = Flex(new_state, default_state["Flex9"])

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		global default_state
		self._Flex32 = Flex(new_state, default_state["Flex32"])

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		global default_state
		self._Flex40 = Flex(new_state, default_state["Flex40"])

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		global default_state
		self._Flex41 = Flex(new_state, default_state["Flex41"])

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		global default_state
		self._Flex45 = Flex(new_state, default_state["Flex45"])

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		global default_state
		self._Flex46 = Flex(new_state, default_state["Flex46"])

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		global default_state
		self._Flex47 = Flex(new_state, default_state["Flex47"])

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		global default_state
		self._Flex48 = Flex(new_state, default_state["Flex48"])

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		global default_state
		self._Flex33 = Flex(new_state, default_state["Flex33"])

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		global default_state
		self._Flex35 = Flex(new_state, default_state["Flex35"])

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		global default_state
		self._Flex36 = Flex(new_state, default_state["Flex36"])

	@property
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		global default_state
		self._Flex37 = Flex(new_state, default_state["Flex37"])

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		global default_state
		self._Flex38 = Flex(new_state, default_state["Flex38"])

	@property
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		global default_state
		self._Flex39 = Flex(new_state, default_state["Flex39"])

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		global default_state
		self._Flex55 = Flex(new_state, default_state["Flex55"])

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		global default_state
		self._Flex56 = Flex(new_state, default_state["Flex56"])

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		global default_state
		self._Flex61 = Flex(new_state, default_state["Flex61"])

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		global default_state
		self._Flex57 = Flex(new_state, default_state["Flex57"])

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		global default_state
		self._Flex58 = Flex(new_state, default_state["Flex58"])

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		global default_state
		self._Flex64 = Flex(new_state, default_state["Flex64"])

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		global default_state
		self._Flex67 = Flex(new_state, default_state["Flex67"])

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		global default_state
		self._Flex68 = Flex(new_state, default_state["Flex68"])

	@property
	def Flex85(self):
		self._getter_access_tracker["Flex85"] = {}
		return self._Flex85
	@Flex85.setter
	def Flex85(self, new_state):
		self._setter_access_tracker["Flex85"] = {}
		global default_state
		self._Flex85 = Flex(new_state, default_state["Flex85"])

	@property
	def Flex86(self):
		self._getter_access_tracker["Flex86"] = {}
		return self._Flex86
	@Flex86.setter
	def Flex86(self, new_state):
		self._setter_access_tracker["Flex86"] = {}
		global default_state
		self._Flex86 = Flex(new_state, default_state["Flex86"])

	@property
	def Flex87(self):
		self._getter_access_tracker["Flex87"] = {}
		return self._Flex87
	@Flex87.setter
	def Flex87(self, new_state):
		self._setter_access_tracker["Flex87"] = {}
		global default_state
		self._Flex87 = Flex(new_state, default_state["Flex87"])

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		global default_state
		self._Flex62 = Flex(new_state, default_state["Flex62"])

	@property
	def Flex71(self):
		self._getter_access_tracker["Flex71"] = {}
		return self._Flex71
	@Flex71.setter
	def Flex71(self, new_state):
		self._setter_access_tracker["Flex71"] = {}
		global default_state
		self._Flex71 = Flex(new_state, default_state["Flex71"])

	@property
	def Flex88(self):
		self._getter_access_tracker["Flex88"] = {}
		return self._Flex88
	@Flex88.setter
	def Flex88(self, new_state):
		self._setter_access_tracker["Flex88"] = {}
		global default_state
		self._Flex88 = Flex(new_state, default_state["Flex88"])

	@property
	def Flex93(self):
		self._getter_access_tracker["Flex93"] = {}
		return self._Flex93
	@Flex93.setter
	def Flex93(self, new_state):
		self._setter_access_tracker["Flex93"] = {}
		global default_state
		self._Flex93 = Flex(new_state, default_state["Flex93"])

	@property
	def Flex94(self):
		self._getter_access_tracker["Flex94"] = {}
		return self._Flex94
	@Flex94.setter
	def Flex94(self, new_state):
		self._setter_access_tracker["Flex94"] = {}
		global default_state
		self._Flex94 = Flex(new_state, default_state["Flex94"])

	@property
	def Flex100(self):
		self._getter_access_tracker["Flex100"] = {}
		return self._Flex100
	@Flex100.setter
	def Flex100(self, new_state):
		self._setter_access_tracker["Flex100"] = {}
		global default_state
		self._Flex100 = Flex(new_state, default_state["Flex100"])

	@property
	def Flex74(self):
		self._getter_access_tracker["Flex74"] = {}
		return self._Flex74
	@Flex74.setter
	def Flex74(self, new_state):
		self._setter_access_tracker["Flex74"] = {}
		global default_state
		self._Flex74 = Flex(new_state, default_state["Flex74"])

	@property
	def Flex76(self):
		self._getter_access_tracker["Flex76"] = {}
		return self._Flex76
	@Flex76.setter
	def Flex76(self, new_state):
		self._setter_access_tracker["Flex76"] = {}
		global default_state
		self._Flex76 = Flex(new_state, default_state["Flex76"])

	@property
	def Flex79(self):
		self._getter_access_tracker["Flex79"] = {}
		return self._Flex79
	@Flex79.setter
	def Flex79(self, new_state):
		self._setter_access_tracker["Flex79"] = {}
		global default_state
		self._Flex79 = Flex(new_state, default_state["Flex79"])

	@property
	def Flex83(self):
		self._getter_access_tracker["Flex83"] = {}
		return self._Flex83
	@Flex83.setter
	def Flex83(self, new_state):
		self._setter_access_tracker["Flex83"] = {}
		global default_state
		self._Flex83 = Flex(new_state, default_state["Flex83"])

	@property
	def Flex84(self):
		self._getter_access_tracker["Flex84"] = {}
		return self._Flex84
	@Flex84.setter
	def Flex84(self, new_state):
		self._setter_access_tracker["Flex84"] = {}
		global default_state
		self._Flex84 = Flex(new_state, default_state["Flex84"])

	@property
	def Flex89(self):
		self._getter_access_tracker["Flex89"] = {}
		return self._Flex89
	@Flex89.setter
	def Flex89(self, new_state):
		self._setter_access_tracker["Flex89"] = {}
		global default_state
		self._Flex89 = Flex(new_state, default_state["Flex89"])

	@property
	def Flex90(self):
		self._getter_access_tracker["Flex90"] = {}
		return self._Flex90
	@Flex90.setter
	def Flex90(self, new_state):
		self._setter_access_tracker["Flex90"] = {}
		global default_state
		self._Flex90 = Flex(new_state, default_state["Flex90"])

	@property
	def Flex91(self):
		self._getter_access_tracker["Flex91"] = {}
		return self._Flex91
	@Flex91.setter
	def Flex91(self, new_state):
		self._setter_access_tracker["Flex91"] = {}
		global default_state
		self._Flex91 = Flex(new_state, default_state["Flex91"])

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		global default_state
		self._Flex60 = Flex(new_state, default_state["Flex60"])

	@property
	def Flex101(self):
		self._getter_access_tracker["Flex101"] = {}
		return self._Flex101
	@Flex101.setter
	def Flex101(self, new_state):
		self._setter_access_tracker["Flex101"] = {}
		global default_state
		self._Flex101 = Flex(new_state, default_state["Flex101"])

	@property
	def Flex102(self):
		self._getter_access_tracker["Flex102"] = {}
		return self._Flex102
	@Flex102.setter
	def Flex102(self, new_state):
		self._setter_access_tracker["Flex102"] = {}
		global default_state
		self._Flex102 = Flex(new_state, default_state["Flex102"])

	@property
	def Flex104(self):
		self._getter_access_tracker["Flex104"] = {}
		return self._Flex104
	@Flex104.setter
	def Flex104(self, new_state):
		self._setter_access_tracker["Flex104"] = {}
		global default_state
		self._Flex104 = Flex(new_state, default_state["Flex104"])

	@property
	def Flex105(self):
		self._getter_access_tracker["Flex105"] = {}
		return self._Flex105
	@Flex105.setter
	def Flex105(self, new_state):
		self._setter_access_tracker["Flex105"] = {}
		global default_state
		self._Flex105 = Flex(new_state, default_state["Flex105"])

	@property
	def Flex106(self):
		self._getter_access_tracker["Flex106"] = {}
		return self._Flex106
	@Flex106.setter
	def Flex106(self, new_state):
		self._setter_access_tracker["Flex106"] = {}
		global default_state
		self._Flex106 = Flex(new_state, default_state["Flex106"])

	@property
	def Flex107(self):
		self._getter_access_tracker["Flex107"] = {}
		return self._Flex107
	@Flex107.setter
	def Flex107(self, new_state):
		self._setter_access_tracker["Flex107"] = {}
		global default_state
		self._Flex107 = Flex(new_state, default_state["Flex107"])

	@property
	def Flex103(self):
		self._getter_access_tracker["Flex103"] = {}
		return self._Flex103
	@Flex103.setter
	def Flex103(self, new_state):
		self._setter_access_tracker["Flex103"] = {}
		global default_state
		self._Flex103 = Flex(new_state, default_state["Flex103"])

	@property
	def Flex108(self):
		self._getter_access_tracker["Flex108"] = {}
		return self._Flex108
	@Flex108.setter
	def Flex108(self, new_state):
		self._setter_access_tracker["Flex108"] = {}
		global default_state
		self._Flex108 = Flex(new_state, default_state["Flex108"])

	@property
	def Flex113(self):
		self._getter_access_tracker["Flex113"] = {}
		return self._Flex113
	@Flex113.setter
	def Flex113(self, new_state):
		self._setter_access_tracker["Flex113"] = {}
		global default_state
		self._Flex113 = Flex(new_state, default_state["Flex113"])

	@property
	def Flex109(self):
		self._getter_access_tracker["Flex109"] = {}
		return self._Flex109
	@Flex109.setter
	def Flex109(self, new_state):
		self._setter_access_tracker["Flex109"] = {}
		global default_state
		self._Flex109 = Flex(new_state, default_state["Flex109"])

	@property
	def Flex114(self):
		self._getter_access_tracker["Flex114"] = {}
		return self._Flex114
	@Flex114.setter
	def Flex114(self, new_state):
		self._setter_access_tracker["Flex114"] = {}
		global default_state
		self._Flex114 = Flex(new_state, default_state["Flex114"])

	@property
	def Flex115(self):
		self._getter_access_tracker["Flex115"] = {}
		return self._Flex115
	@Flex115.setter
	def Flex115(self, new_state):
		self._setter_access_tracker["Flex115"] = {}
		global default_state
		self._Flex115 = Flex(new_state, default_state["Flex115"])

	@property
	def Flex116(self):
		self._getter_access_tracker["Flex116"] = {}
		return self._Flex116
	@Flex116.setter
	def Flex116(self, new_state):
		self._setter_access_tracker["Flex116"] = {}
		global default_state
		self._Flex116 = Flex(new_state, default_state["Flex116"])

	@property
	def Flex110(self):
		self._getter_access_tracker["Flex110"] = {}
		return self._Flex110
	@Flex110.setter
	def Flex110(self, new_state):
		self._setter_access_tracker["Flex110"] = {}
		global default_state
		self._Flex110 = Flex(new_state, default_state["Flex110"])

	@property
	def Flex117(self):
		self._getter_access_tracker["Flex117"] = {}
		return self._Flex117
	@Flex117.setter
	def Flex117(self, new_state):
		self._setter_access_tracker["Flex117"] = {}
		global default_state
		self._Flex117 = Flex(new_state, default_state["Flex117"])

	@property
	def Flex118(self):
		self._getter_access_tracker["Flex118"] = {}
		return self._Flex118
	@Flex118.setter
	def Flex118(self, new_state):
		self._setter_access_tracker["Flex118"] = {}
		global default_state
		self._Flex118 = Flex(new_state, default_state["Flex118"])

	@property
	def Flex119(self):
		self._getter_access_tracker["Flex119"] = {}
		return self._Flex119
	@Flex119.setter
	def Flex119(self, new_state):
		self._setter_access_tracker["Flex119"] = {}
		global default_state
		self._Flex119 = Flex(new_state, default_state["Flex119"])

	@property
	def Flex111(self):
		self._getter_access_tracker["Flex111"] = {}
		return self._Flex111
	@Flex111.setter
	def Flex111(self, new_state):
		self._setter_access_tracker["Flex111"] = {}
		global default_state
		self._Flex111 = Flex(new_state, default_state["Flex111"])

	@property
	def Flex120(self):
		self._getter_access_tracker["Flex120"] = {}
		return self._Flex120
	@Flex120.setter
	def Flex120(self, new_state):
		self._setter_access_tracker["Flex120"] = {}
		global default_state
		self._Flex120 = Flex(new_state, default_state["Flex120"])

	@property
	def Flex121(self):
		self._getter_access_tracker["Flex121"] = {}
		return self._Flex121
	@Flex121.setter
	def Flex121(self, new_state):
		self._setter_access_tracker["Flex121"] = {}
		global default_state
		self._Flex121 = Flex(new_state, default_state["Flex121"])

	@property
	def Flex122(self):
		self._getter_access_tracker["Flex122"] = {}
		return self._Flex122
	@Flex122.setter
	def Flex122(self, new_state):
		self._setter_access_tracker["Flex122"] = {}
		global default_state
		self._Flex122 = Flex(new_state, default_state["Flex122"])

	@property
	def Flex112(self):
		self._getter_access_tracker["Flex112"] = {}
		return self._Flex112
	@Flex112.setter
	def Flex112(self, new_state):
		self._setter_access_tracker["Flex112"] = {}
		global default_state
		self._Flex112 = Flex(new_state, default_state["Flex112"])

	@property
	def Flex123(self):
		self._getter_access_tracker["Flex123"] = {}
		return self._Flex123
	@Flex123.setter
	def Flex123(self, new_state):
		self._setter_access_tracker["Flex123"] = {}
		global default_state
		self._Flex123 = Flex(new_state, default_state["Flex123"])

	@property
	def Flex124(self):
		self._getter_access_tracker["Flex124"] = {}
		return self._Flex124
	@Flex124.setter
	def Flex124(self, new_state):
		self._setter_access_tracker["Flex124"] = {}
		global default_state
		self._Flex124 = Flex(new_state, default_state["Flex124"])

	@property
	def Flex125(self):
		self._getter_access_tracker["Flex125"] = {}
		return self._Flex125
	@Flex125.setter
	def Flex125(self, new_state):
		self._setter_access_tracker["Flex125"] = {}
		global default_state
		self._Flex125 = Flex(new_state, default_state["Flex125"])

	@property
	def Flex129(self):
		self._getter_access_tracker["Flex129"] = {}
		return self._Flex129
	@Flex129.setter
	def Flex129(self, new_state):
		self._setter_access_tracker["Flex129"] = {}
		global default_state
		self._Flex129 = Flex(new_state, default_state["Flex129"])

	@property
	def Flex128(self):
		self._getter_access_tracker["Flex128"] = {}
		return self._Flex128
	@Flex128.setter
	def Flex128(self, new_state):
		self._setter_access_tracker["Flex128"] = {}
		global default_state
		self._Flex128 = Flex(new_state, default_state["Flex128"])

	@property
	def Flex132(self):
		self._getter_access_tracker["Flex132"] = {}
		return self._Flex132
	@Flex132.setter
	def Flex132(self, new_state):
		self._setter_access_tracker["Flex132"] = {}
		global default_state
		self._Flex132 = Flex(new_state, default_state["Flex132"])

	@property
	def Flex133(self):
		self._getter_access_tracker["Flex133"] = {}
		return self._Flex133
	@Flex133.setter
	def Flex133(self, new_state):
		self._setter_access_tracker["Flex133"] = {}
		global default_state
		self._Flex133 = Flex(new_state, default_state["Flex133"])

	@property
	def Flex130(self):
		self._getter_access_tracker["Flex130"] = {}
		return self._Flex130
	@Flex130.setter
	def Flex130(self, new_state):
		self._setter_access_tracker["Flex130"] = {}
		global default_state
		self._Flex130 = Flex(new_state, default_state["Flex130"])

	@property
	def Flex134(self):
		self._getter_access_tracker["Flex134"] = {}
		return self._Flex134
	@Flex134.setter
	def Flex134(self, new_state):
		self._setter_access_tracker["Flex134"] = {}
		global default_state
		self._Flex134 = Flex(new_state, default_state["Flex134"])

	@property
	def Flex135(self):
		self._getter_access_tracker["Flex135"] = {}
		return self._Flex135
	@Flex135.setter
	def Flex135(self, new_state):
		self._setter_access_tracker["Flex135"] = {}
		global default_state
		self._Flex135 = Flex(new_state, default_state["Flex135"])

	@property
	def Flex137(self):
		self._getter_access_tracker["Flex137"] = {}
		return self._Flex137
	@Flex137.setter
	def Flex137(self, new_state):
		self._setter_access_tracker["Flex137"] = {}
		global default_state
		self._Flex137 = Flex(new_state, default_state["Flex137"])

	@property
	def Flex138(self):
		self._getter_access_tracker["Flex138"] = {}
		return self._Flex138
	@Flex138.setter
	def Flex138(self, new_state):
		self._setter_access_tracker["Flex138"] = {}
		global default_state
		self._Flex138 = Flex(new_state, default_state["Flex138"])

	@property
	def Flex136(self):
		self._getter_access_tracker["Flex136"] = {}
		return self._Flex136
	@Flex136.setter
	def Flex136(self, new_state):
		self._setter_access_tracker["Flex136"] = {}
		global default_state
		self._Flex136 = Flex(new_state, default_state["Flex136"])

	@property
	def Flex139(self):
		self._getter_access_tracker["Flex139"] = {}
		return self._Flex139
	@Flex139.setter
	def Flex139(self, new_state):
		self._setter_access_tracker["Flex139"] = {}
		global default_state
		self._Flex139 = Flex(new_state, default_state["Flex139"])

	@property
	def Flex140(self):
		self._getter_access_tracker["Flex140"] = {}
		return self._Flex140
	@Flex140.setter
	def Flex140(self, new_state):
		self._setter_access_tracker["Flex140"] = {}
		global default_state
		self._Flex140 = Flex(new_state, default_state["Flex140"])

	@property
	def Flex143(self):
		self._getter_access_tracker["Flex143"] = {}
		return self._Flex143
	@Flex143.setter
	def Flex143(self, new_state):
		self._setter_access_tracker["Flex143"] = {}
		global default_state
		self._Flex143 = Flex(new_state, default_state["Flex143"])

	@property
	def Flex144(self):
		self._getter_access_tracker["Flex144"] = {}
		return self._Flex144
	@Flex144.setter
	def Flex144(self, new_state):
		self._setter_access_tracker["Flex144"] = {}
		global default_state
		self._Flex144 = Flex(new_state, default_state["Flex144"])

	@property
	def Flex146(self):
		self._getter_access_tracker["Flex146"] = {}
		return self._Flex146
	@Flex146.setter
	def Flex146(self, new_state):
		self._setter_access_tracker["Flex146"] = {}
		global default_state
		self._Flex146 = Flex(new_state, default_state["Flex146"])

	@property
	def Flex158(self):
		self._getter_access_tracker["Flex158"] = {}
		return self._Flex158
	@Flex158.setter
	def Flex158(self, new_state):
		self._setter_access_tracker["Flex158"] = {}
		global default_state
		self._Flex158 = Flex(new_state, default_state["Flex158"])

	@property
	def Flex164(self):
		self._getter_access_tracker["Flex164"] = {}
		return self._Flex164
	@Flex164.setter
	def Flex164(self, new_state):
		self._setter_access_tracker["Flex164"] = {}
		global default_state
		self._Flex164 = Flex(new_state, default_state["Flex164"])

	@property
	def Flex165(self):
		self._getter_access_tracker["Flex165"] = {}
		return self._Flex165
	@Flex165.setter
	def Flex165(self, new_state):
		self._setter_access_tracker["Flex165"] = {}
		global default_state
		self._Flex165 = Flex(new_state, default_state["Flex165"])

	@property
	def Flex159(self):
		self._getter_access_tracker["Flex159"] = {}
		return self._Flex159
	@Flex159.setter
	def Flex159(self, new_state):
		self._setter_access_tracker["Flex159"] = {}
		global default_state
		self._Flex159 = Flex(new_state, default_state["Flex159"])

	@property
	def Flex166(self):
		self._getter_access_tracker["Flex166"] = {}
		return self._Flex166
	@Flex166.setter
	def Flex166(self, new_state):
		self._setter_access_tracker["Flex166"] = {}
		global default_state
		self._Flex166 = Flex(new_state, default_state["Flex166"])

	@property
	def Flex167(self):
		self._getter_access_tracker["Flex167"] = {}
		return self._Flex167
	@Flex167.setter
	def Flex167(self, new_state):
		self._setter_access_tracker["Flex167"] = {}
		global default_state
		self._Flex167 = Flex(new_state, default_state["Flex167"])

	@property
	def Flex147(self):
		self._getter_access_tracker["Flex147"] = {}
		return self._Flex147
	@Flex147.setter
	def Flex147(self, new_state):
		self._setter_access_tracker["Flex147"] = {}
		global default_state
		self._Flex147 = Flex(new_state, default_state["Flex147"])

	@property
	def Flex154(self):
		self._getter_access_tracker["Flex154"] = {}
		return self._Flex154
	@Flex154.setter
	def Flex154(self, new_state):
		self._setter_access_tracker["Flex154"] = {}
		global default_state
		self._Flex154 = Flex(new_state, default_state["Flex154"])

	@property
	def Flex155(self):
		self._getter_access_tracker["Flex155"] = {}
		return self._Flex155
	@Flex155.setter
	def Flex155(self, new_state):
		self._setter_access_tracker["Flex155"] = {}
		global default_state
		self._Flex155 = Flex(new_state, default_state["Flex155"])

	@property
	def Flex148(self):
		self._getter_access_tracker["Flex148"] = {}
		return self._Flex148
	@Flex148.setter
	def Flex148(self, new_state):
		self._setter_access_tracker["Flex148"] = {}
		global default_state
		self._Flex148 = Flex(new_state, default_state["Flex148"])

	@property
	def Flex160(self):
		self._getter_access_tracker["Flex160"] = {}
		return self._Flex160
	@Flex160.setter
	def Flex160(self, new_state):
		self._setter_access_tracker["Flex160"] = {}
		global default_state
		self._Flex160 = Flex(new_state, default_state["Flex160"])

	@property
	def Flex173(self):
		self._getter_access_tracker["Flex173"] = {}
		return self._Flex173
	@Flex173.setter
	def Flex173(self, new_state):
		self._setter_access_tracker["Flex173"] = {}
		global default_state
		self._Flex173 = Flex(new_state, default_state["Flex173"])

	@property
	def Flex171(self):
		self._getter_access_tracker["Flex171"] = {}
		return self._Flex171
	@Flex171.setter
	def Flex171(self, new_state):
		self._setter_access_tracker["Flex171"] = {}
		global default_state
		self._Flex171 = Flex(new_state, default_state["Flex171"])

	@property
	def Flex172(self):
		self._getter_access_tracker["Flex172"] = {}
		return self._Flex172
	@Flex172.setter
	def Flex172(self, new_state):
		self._setter_access_tracker["Flex172"] = {}
		global default_state
		self._Flex172 = Flex(new_state, default_state["Flex172"])

	@property
	def Flex149(self):
		self._getter_access_tracker["Flex149"] = {}
		return self._Flex149
	@Flex149.setter
	def Flex149(self, new_state):
		self._setter_access_tracker["Flex149"] = {}
		global default_state
		self._Flex149 = Flex(new_state, default_state["Flex149"])

	@property
	def Flex162(self):
		self._getter_access_tracker["Flex162"] = {}
		return self._Flex162
	@Flex162.setter
	def Flex162(self, new_state):
		self._setter_access_tracker["Flex162"] = {}
		global default_state
		self._Flex162 = Flex(new_state, default_state["Flex162"])

	@property
	def Flex176(self):
		self._getter_access_tracker["Flex176"] = {}
		return self._Flex176
	@Flex176.setter
	def Flex176(self, new_state):
		self._setter_access_tracker["Flex176"] = {}
		global default_state
		self._Flex176 = Flex(new_state, default_state["Flex176"])

	@property
	def Flex174(self):
		self._getter_access_tracker["Flex174"] = {}
		return self._Flex174
	@Flex174.setter
	def Flex174(self, new_state):
		self._setter_access_tracker["Flex174"] = {}
		global default_state
		self._Flex174 = Flex(new_state, default_state["Flex174"])

	@property
	def Flex175(self):
		self._getter_access_tracker["Flex175"] = {}
		return self._Flex175
	@Flex175.setter
	def Flex175(self, new_state):
		self._setter_access_tracker["Flex175"] = {}
		global default_state
		self._Flex175 = Flex(new_state, default_state["Flex175"])

	@property
	def Flex145(self):
		self._getter_access_tracker["Flex145"] = {}
		return self._Flex145
	@Flex145.setter
	def Flex145(self, new_state):
		self._setter_access_tracker["Flex145"] = {}
		global default_state
		self._Flex145 = Flex(new_state, default_state["Flex145"])

	@property
	def Flex152(self):
		self._getter_access_tracker["Flex152"] = {}
		return self._Flex152
	@Flex152.setter
	def Flex152(self, new_state):
		self._setter_access_tracker["Flex152"] = {}
		global default_state
		self._Flex152 = Flex(new_state, default_state["Flex152"])

	@property
	def Flex204(self):
		self._getter_access_tracker["Flex204"] = {}
		return self._Flex204
	@Flex204.setter
	def Flex204(self, new_state):
		self._setter_access_tracker["Flex204"] = {}
		global default_state
		self._Flex204 = Flex(new_state, default_state["Flex204"])

	@property
	def Flex202(self):
		self._getter_access_tracker["Flex202"] = {}
		return self._Flex202
	@Flex202.setter
	def Flex202(self, new_state):
		self._setter_access_tracker["Flex202"] = {}
		global default_state
		self._Flex202 = Flex(new_state, default_state["Flex202"])

	@property
	def Flex198(self):
		self._getter_access_tracker["Flex198"] = {}
		return self._Flex198
	@Flex198.setter
	def Flex198(self, new_state):
		self._setter_access_tracker["Flex198"] = {}
		global default_state
		self._Flex198 = Flex(new_state, default_state["Flex198"])

	@property
	def Flex199(self):
		self._getter_access_tracker["Flex199"] = {}
		return self._Flex199
	@Flex199.setter
	def Flex199(self, new_state):
		self._setter_access_tracker["Flex199"] = {}
		global default_state
		self._Flex199 = Flex(new_state, default_state["Flex199"])

	@property
	def Flex203(self):
		self._getter_access_tracker["Flex203"] = {}
		return self._Flex203
	@Flex203.setter
	def Flex203(self, new_state):
		self._setter_access_tracker["Flex203"] = {}
		global default_state
		self._Flex203 = Flex(new_state, default_state["Flex203"])

	@property
	def Flex200(self):
		self._getter_access_tracker["Flex200"] = {}
		return self._Flex200
	@Flex200.setter
	def Flex200(self, new_state):
		self._setter_access_tracker["Flex200"] = {}
		global default_state
		self._Flex200 = Flex(new_state, default_state["Flex200"])

	@property
	def Flex201(self):
		self._getter_access_tracker["Flex201"] = {}
		return self._Flex201
	@Flex201.setter
	def Flex201(self, new_state):
		self._setter_access_tracker["Flex201"] = {}
		global default_state
		self._Flex201 = Flex(new_state, default_state["Flex201"])

	@property
	def Flex153(self):
		self._getter_access_tracker["Flex153"] = {}
		return self._Flex153
	@Flex153.setter
	def Flex153(self, new_state):
		self._setter_access_tracker["Flex153"] = {}
		global default_state
		self._Flex153 = Flex(new_state, default_state["Flex153"])

	@property
	def Flex156(self):
		self._getter_access_tracker["Flex156"] = {}
		return self._Flex156
	@Flex156.setter
	def Flex156(self, new_state):
		self._setter_access_tracker["Flex156"] = {}
		global default_state
		self._Flex156 = Flex(new_state, default_state["Flex156"])

	@property
	def Flex157(self):
		self._getter_access_tracker["Flex157"] = {}
		return self._Flex157
	@Flex157.setter
	def Flex157(self, new_state):
		self._setter_access_tracker["Flex157"] = {}
		global default_state
		self._Flex157 = Flex(new_state, default_state["Flex157"])

	@property
	def Flex232(self):
		self._getter_access_tracker["Flex232"] = {}
		return self._Flex232
	@Flex232.setter
	def Flex232(self, new_state):
		self._setter_access_tracker["Flex232"] = {}
		global default_state
		self._Flex232 = Flex(new_state, default_state["Flex232"])

	@property
	def Flex230(self):
		self._getter_access_tracker["Flex230"] = {}
		return self._Flex230
	@Flex230.setter
	def Flex230(self, new_state):
		self._setter_access_tracker["Flex230"] = {}
		global default_state
		self._Flex230 = Flex(new_state, default_state["Flex230"])

	@property
	def Flex226(self):
		self._getter_access_tracker["Flex226"] = {}
		return self._Flex226
	@Flex226.setter
	def Flex226(self, new_state):
		self._setter_access_tracker["Flex226"] = {}
		global default_state
		self._Flex226 = Flex(new_state, default_state["Flex226"])

	@property
	def Flex227(self):
		self._getter_access_tracker["Flex227"] = {}
		return self._Flex227
	@Flex227.setter
	def Flex227(self, new_state):
		self._setter_access_tracker["Flex227"] = {}
		global default_state
		self._Flex227 = Flex(new_state, default_state["Flex227"])

	@property
	def Flex231(self):
		self._getter_access_tracker["Flex231"] = {}
		return self._Flex231
	@Flex231.setter
	def Flex231(self, new_state):
		self._setter_access_tracker["Flex231"] = {}
		global default_state
		self._Flex231 = Flex(new_state, default_state["Flex231"])

	@property
	def Flex228(self):
		self._getter_access_tracker["Flex228"] = {}
		return self._Flex228
	@Flex228.setter
	def Flex228(self, new_state):
		self._setter_access_tracker["Flex228"] = {}
		global default_state
		self._Flex228 = Flex(new_state, default_state["Flex228"])

	@property
	def Flex229(self):
		self._getter_access_tracker["Flex229"] = {}
		return self._Flex229
	@Flex229.setter
	def Flex229(self, new_state):
		self._setter_access_tracker["Flex229"] = {}
		global default_state
		self._Flex229 = Flex(new_state, default_state["Flex229"])

	@property
	def Flex239(self):
		self._getter_access_tracker["Flex239"] = {}
		return self._Flex239
	@Flex239.setter
	def Flex239(self, new_state):
		self._setter_access_tracker["Flex239"] = {}
		global default_state
		self._Flex239 = Flex(new_state, default_state["Flex239"])

	@property
	def Flex237(self):
		self._getter_access_tracker["Flex237"] = {}
		return self._Flex237
	@Flex237.setter
	def Flex237(self, new_state):
		self._setter_access_tracker["Flex237"] = {}
		global default_state
		self._Flex237 = Flex(new_state, default_state["Flex237"])

	@property
	def Flex233(self):
		self._getter_access_tracker["Flex233"] = {}
		return self._Flex233
	@Flex233.setter
	def Flex233(self, new_state):
		self._setter_access_tracker["Flex233"] = {}
		global default_state
		self._Flex233 = Flex(new_state, default_state["Flex233"])

	@property
	def Flex234(self):
		self._getter_access_tracker["Flex234"] = {}
		return self._Flex234
	@Flex234.setter
	def Flex234(self, new_state):
		self._setter_access_tracker["Flex234"] = {}
		global default_state
		self._Flex234 = Flex(new_state, default_state["Flex234"])

	@property
	def Flex238(self):
		self._getter_access_tracker["Flex238"] = {}
		return self._Flex238
	@Flex238.setter
	def Flex238(self, new_state):
		self._setter_access_tracker["Flex238"] = {}
		global default_state
		self._Flex238 = Flex(new_state, default_state["Flex238"])

	@property
	def Flex235(self):
		self._getter_access_tracker["Flex235"] = {}
		return self._Flex235
	@Flex235.setter
	def Flex235(self, new_state):
		self._setter_access_tracker["Flex235"] = {}
		global default_state
		self._Flex235 = Flex(new_state, default_state["Flex235"])

	@property
	def Flex236(self):
		self._getter_access_tracker["Flex236"] = {}
		return self._Flex236
	@Flex236.setter
	def Flex236(self, new_state):
		self._setter_access_tracker["Flex236"] = {}
		global default_state
		self._Flex236 = Flex(new_state, default_state["Flex236"])

	@property
	def Flex240(self):
		self._getter_access_tracker["Flex240"] = {}
		return self._Flex240
	@Flex240.setter
	def Flex240(self, new_state):
		self._setter_access_tracker["Flex240"] = {}
		global default_state
		self._Flex240 = Flex(new_state, default_state["Flex240"])

	@property
	def Flex245(self):
		self._getter_access_tracker["Flex245"] = {}
		return self._Flex245
	@Flex245.setter
	def Flex245(self, new_state):
		self._setter_access_tracker["Flex245"] = {}
		global default_state
		self._Flex245 = Flex(new_state, default_state["Flex245"])

	@property
	def Flex246(self):
		self._getter_access_tracker["Flex246"] = {}
		return self._Flex246
	@Flex246.setter
	def Flex246(self, new_state):
		self._setter_access_tracker["Flex246"] = {}
		global default_state
		self._Flex246 = Flex(new_state, default_state["Flex246"])

	@property
	def Flex249(self):
		self._getter_access_tracker["Flex249"] = {}
		return self._Flex249
	@Flex249.setter
	def Flex249(self, new_state):
		self._setter_access_tracker["Flex249"] = {}
		global default_state
		self._Flex249 = Flex(new_state, default_state["Flex249"])

	@property
	def Flex252(self):
		self._getter_access_tracker["Flex252"] = {}
		return self._Flex252
	@Flex252.setter
	def Flex252(self, new_state):
		self._setter_access_tracker["Flex252"] = {}
		global default_state
		self._Flex252 = Flex(new_state, default_state["Flex252"])

	@property
	def Flex248(self):
		self._getter_access_tracker["Flex248"] = {}
		return self._Flex248
	@Flex248.setter
	def Flex248(self, new_state):
		self._setter_access_tracker["Flex248"] = {}
		global default_state
		self._Flex248 = Flex(new_state, default_state["Flex248"])

	@property
	def Flex244(self):
		self._getter_access_tracker["Flex244"] = {}
		return self._Flex244
	@Flex244.setter
	def Flex244(self, new_state):
		self._setter_access_tracker["Flex244"] = {}
		global default_state
		self._Flex244 = Flex(new_state, default_state["Flex244"])

	@property
	def Flex241(self):
		self._getter_access_tracker["Flex241"] = {}
		return self._Flex241
	@Flex241.setter
	def Flex241(self, new_state):
		self._setter_access_tracker["Flex241"] = {}
		global default_state
		self._Flex241 = Flex(new_state, default_state["Flex241"])

	@property
	def Flex242(self):
		self._getter_access_tracker["Flex242"] = {}
		return self._Flex242
	@Flex242.setter
	def Flex242(self, new_state):
		self._setter_access_tracker["Flex242"] = {}
		global default_state
		self._Flex242 = Flex(new_state, default_state["Flex242"])

	@property
	def Flex243(self):
		self._getter_access_tracker["Flex243"] = {}
		return self._Flex243
	@Flex243.setter
	def Flex243(self, new_state):
		self._setter_access_tracker["Flex243"] = {}
		global default_state
		self._Flex243 = Flex(new_state, default_state["Flex243"])

	@property
	def Flex253(self):
		self._getter_access_tracker["Flex253"] = {}
		return self._Flex253
	@Flex253.setter
	def Flex253(self, new_state):
		self._setter_access_tracker["Flex253"] = {}
		global default_state
		self._Flex253 = Flex(new_state, default_state["Flex253"])

	@property
	def Flex254(self):
		self._getter_access_tracker["Flex254"] = {}
		return self._Flex254
	@Flex254.setter
	def Flex254(self, new_state):
		self._setter_access_tracker["Flex254"] = {}
		global default_state
		self._Flex254 = Flex(new_state, default_state["Flex254"])

	@property
	def Flex255(self):
		self._getter_access_tracker["Flex255"] = {}
		return self._Flex255
	@Flex255.setter
	def Flex255(self, new_state):
		self._setter_access_tracker["Flex255"] = {}
		global default_state
		self._Flex255 = Flex(new_state, default_state["Flex255"])

	@property
	def Flex256(self):
		self._getter_access_tracker["Flex256"] = {}
		return self._Flex256
	@Flex256.setter
	def Flex256(self, new_state):
		self._setter_access_tracker["Flex256"] = {}
		global default_state
		self._Flex256 = Flex(new_state, default_state["Flex256"])

	@property
	def Flex257(self):
		self._getter_access_tracker["Flex257"] = {}
		return self._Flex257
	@Flex257.setter
	def Flex257(self, new_state):
		self._setter_access_tracker["Flex257"] = {}
		global default_state
		self._Flex257 = Flex(new_state, default_state["Flex257"])

	@property
	def Flex278(self):
		self._getter_access_tracker["Flex278"] = {}
		return self._Flex278
	@Flex278.setter
	def Flex278(self, new_state):
		self._setter_access_tracker["Flex278"] = {}
		global default_state
		self._Flex278 = Flex(new_state, default_state["Flex278"])

	@property
	def Flex280(self):
		self._getter_access_tracker["Flex280"] = {}
		return self._Flex280
	@Flex280.setter
	def Flex280(self, new_state):
		self._setter_access_tracker["Flex280"] = {}
		global default_state
		self._Flex280 = Flex(new_state, default_state["Flex280"])

	@property
	def Flex281(self):
		self._getter_access_tracker["Flex281"] = {}
		return self._Flex281
	@Flex281.setter
	def Flex281(self, new_state):
		self._setter_access_tracker["Flex281"] = {}
		global default_state
		self._Flex281 = Flex(new_state, default_state["Flex281"])

	@property
	def Flex258(self):
		self._getter_access_tracker["Flex258"] = {}
		return self._Flex258
	@Flex258.setter
	def Flex258(self, new_state):
		self._setter_access_tracker["Flex258"] = {}
		global default_state
		self._Flex258 = Flex(new_state, default_state["Flex258"])

	@property
	def Flex263(self):
		self._getter_access_tracker["Flex263"] = {}
		return self._Flex263
	@Flex263.setter
	def Flex263(self, new_state):
		self._setter_access_tracker["Flex263"] = {}
		global default_state
		self._Flex263 = Flex(new_state, default_state["Flex263"])

	@property
	def Flex274(self):
		self._getter_access_tracker["Flex274"] = {}
		return self._Flex274
	@Flex274.setter
	def Flex274(self, new_state):
		self._setter_access_tracker["Flex274"] = {}
		global default_state
		self._Flex274 = Flex(new_state, default_state["Flex274"])

	@property
	def Flex279(self):
		self._getter_access_tracker["Flex279"] = {}
		return self._Flex279
	@Flex279.setter
	def Flex279(self, new_state):
		self._setter_access_tracker["Flex279"] = {}
		global default_state
		self._Flex279 = Flex(new_state, default_state["Flex279"])

	@property
	def Flex282(self):
		self._getter_access_tracker["Flex282"] = {}
		return self._Flex282
	@Flex282.setter
	def Flex282(self, new_state):
		self._setter_access_tracker["Flex282"] = {}
		global default_state
		self._Flex282 = Flex(new_state, default_state["Flex282"])

	@property
	def Flex283(self):
		self._getter_access_tracker["Flex283"] = {}
		return self._Flex283
	@Flex283.setter
	def Flex283(self, new_state):
		self._setter_access_tracker["Flex283"] = {}
		global default_state
		self._Flex283 = Flex(new_state, default_state["Flex283"])

	@property
	def Flex296(self):
		self._getter_access_tracker["Flex296"] = {}
		return self._Flex296
	@Flex296.setter
	def Flex296(self, new_state):
		self._setter_access_tracker["Flex296"] = {}
		global default_state
		self._Flex296 = Flex(new_state, default_state["Flex296"])

	@property
	def Flex293(self):
		self._getter_access_tracker["Flex293"] = {}
		return self._Flex293
	@Flex293.setter
	def Flex293(self, new_state):
		self._setter_access_tracker["Flex293"] = {}
		global default_state
		self._Flex293 = Flex(new_state, default_state["Flex293"])

	@property
	def Flex295(self):
		self._getter_access_tracker["Flex295"] = {}
		return self._Flex295
	@Flex295.setter
	def Flex295(self, new_state):
		self._setter_access_tracker["Flex295"] = {}
		global default_state
		self._Flex295 = Flex(new_state, default_state["Flex295"])

	@property
	def Flex294(self):
		self._getter_access_tracker["Flex294"] = {}
		return self._Flex294
	@Flex294.setter
	def Flex294(self, new_state):
		self._setter_access_tracker["Flex294"] = {}
		global default_state
		self._Flex294 = Flex(new_state, default_state["Flex294"])

	@property
	def Flex297(self):
		self._getter_access_tracker["Flex297"] = {}
		return self._Flex297
	@Flex297.setter
	def Flex297(self, new_state):
		self._setter_access_tracker["Flex297"] = {}
		global default_state
		self._Flex297 = Flex(new_state, default_state["Flex297"])

	@property
	def Flex292(self):
		self._getter_access_tracker["Flex292"] = {}
		return self._Flex292
	@Flex292.setter
	def Flex292(self, new_state):
		self._setter_access_tracker["Flex292"] = {}
		global default_state
		self._Flex292 = Flex(new_state, default_state["Flex292"])

	@property
	def Flex291(self):
		self._getter_access_tracker["Flex291"] = {}
		return self._Flex291
	@Flex291.setter
	def Flex291(self, new_state):
		self._setter_access_tracker["Flex291"] = {}
		global default_state
		self._Flex291 = Flex(new_state, default_state["Flex291"])

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		global default_state
		self._TextBox1 = TextBox(new_state, default_state["TextBox1"])

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		global default_state
		self._TextBox17 = TextBox(new_state, default_state["TextBox17"])

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		global default_state
		self._TextBox20 = TextBox(new_state, default_state["TextBox20"])

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		global default_state
		self._TextBox19 = TextBox(new_state, default_state["TextBox19"])

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		global default_state
		self._TextBox18 = TextBox(new_state, default_state["TextBox18"])

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		global default_state
		self._TextBox22 = TextBox(new_state, default_state["TextBox22"])

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		global default_state
		self._Image3 = Image(new_state, default_state["Image3"])

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		global default_state
		self._TextBox23 = TextBox(new_state, default_state["TextBox23"])

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		global default_state
		self._TextBox13 = TextBox(new_state, default_state["TextBox13"])

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		global default_state
		self._TextBox14 = TextBox(new_state, default_state["TextBox14"])

	@property
	def Button4(self):
		self._getter_access_tracker["Button4"] = {}
		return self._Button4
	@Button4.setter
	def Button4(self, new_state):
		self._setter_access_tracker["Button4"] = {}
		global default_state
		self._Button4 = Button(new_state, default_state["Button4"])

	@property
	def Button6(self):
		self._getter_access_tracker["Button6"] = {}
		return self._Button6
	@Button6.setter
	def Button6(self, new_state):
		self._setter_access_tracker["Button6"] = {}
		global default_state
		self._Button6 = Button(new_state, default_state["Button6"])

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		global default_state
		self._Image1 = Image(new_state, default_state["Image1"])

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		global default_state
		self._TextBox29 = TextBox(new_state, default_state["TextBox29"])

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		global default_state
		self._TextBox31 = TextBox(new_state, default_state["TextBox31"])

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		global default_state
		self._Image9 = Image(new_state, default_state["Image9"])

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		global default_state
		self._TextBox33 = TextBox(new_state, default_state["TextBox33"])

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		global default_state
		self._TextBox37 = TextBox(new_state, default_state["TextBox37"])

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		global default_state
		self._Image12 = Image(new_state, default_state["Image12"])

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		global default_state
		self._Image10 = Image(new_state, default_state["Image10"])

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		global default_state
		self._TextBox34 = TextBox(new_state, default_state["TextBox34"])

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		global default_state
		self._TextBox38 = TextBox(new_state, default_state["TextBox38"])

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		global default_state
		self._Image13 = Image(new_state, default_state["Image13"])

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		global default_state
		self._Image11 = Image(new_state, default_state["Image11"])

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		global default_state
		self._TextBox36 = TextBox(new_state, default_state["TextBox36"])

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		global default_state
		self._TextBox39 = TextBox(new_state, default_state["TextBox39"])

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		global default_state
		self._Image14 = Image(new_state, default_state["Image14"])

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		global default_state
		self._TextBox28 = TextBox(new_state, default_state["TextBox28"])

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		global default_state
		self._Image5 = Image(new_state, default_state["Image5"])

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		global default_state
		self._Image6 = Image(new_state, default_state["Image6"])

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		global default_state
		self._Image7 = Image(new_state, default_state["Image7"])

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		global default_state
		self._Image8 = Image(new_state, default_state["Image8"])

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		global default_state
		self._TextBox48 = TextBox(new_state, default_state["TextBox48"])

	@property
	def Button7(self):
		self._getter_access_tracker["Button7"] = {}
		return self._Button7
	@Button7.setter
	def Button7(self, new_state):
		self._setter_access_tracker["Button7"] = {}
		global default_state
		self._Button7 = Button(new_state, default_state["Button7"])

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		global default_state
		self._Image16 = Image(new_state, default_state["Image16"])

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		global default_state
		self._TextBox50 = TextBox(new_state, default_state["TextBox50"])

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		global default_state
		self._TextBox51 = TextBox(new_state, default_state["TextBox51"])

	@property
	def TextBox52(self):
		self._getter_access_tracker["TextBox52"] = {}
		return self._TextBox52
	@TextBox52.setter
	def TextBox52(self, new_state):
		self._setter_access_tracker["TextBox52"] = {}
		global default_state
		self._TextBox52 = TextBox(new_state, default_state["TextBox52"])

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		global default_state
		self._Image19 = Image(new_state, default_state["Image19"])

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		global default_state
		self._Image17 = Image(new_state, default_state["Image17"])

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		global default_state
		self._TextBox54 = TextBox(new_state, default_state["TextBox54"])

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		global default_state
		self._TextBox59 = TextBox(new_state, default_state["TextBox59"])

	@property
	def TextBox53(self):
		self._getter_access_tracker["TextBox53"] = {}
		return self._TextBox53
	@TextBox53.setter
	def TextBox53(self, new_state):
		self._setter_access_tracker["TextBox53"] = {}
		global default_state
		self._TextBox53 = TextBox(new_state, default_state["TextBox53"])

	@property
	def TextBox62(self):
		self._getter_access_tracker["TextBox62"] = {}
		return self._TextBox62
	@TextBox62.setter
	def TextBox62(self, new_state):
		self._setter_access_tracker["TextBox62"] = {}
		global default_state
		self._TextBox62 = TextBox(new_state, default_state["TextBox62"])

	@property
	def Image22(self):
		self._getter_access_tracker["Image22"] = {}
		return self._Image22
	@Image22.setter
	def Image22(self, new_state):
		self._setter_access_tracker["Image22"] = {}
		global default_state
		self._Image22 = Image(new_state, default_state["Image22"])

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		global default_state
		self._Image18 = Image(new_state, default_state["Image18"])

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		global default_state
		self._TextBox56 = TextBox(new_state, default_state["TextBox56"])

	@property
	def TextBox55(self):
		self._getter_access_tracker["TextBox55"] = {}
		return self._TextBox55
	@TextBox55.setter
	def TextBox55(self, new_state):
		self._setter_access_tracker["TextBox55"] = {}
		global default_state
		self._TextBox55 = TextBox(new_state, default_state["TextBox55"])

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		global default_state
		self._Image21 = Image(new_state, default_state["Image21"])

	@property
	def TextBox57(self):
		self._getter_access_tracker["TextBox57"] = {}
		return self._TextBox57
	@TextBox57.setter
	def TextBox57(self, new_state):
		self._setter_access_tracker["TextBox57"] = {}
		global default_state
		self._TextBox57 = TextBox(new_state, default_state["TextBox57"])

	@property
	def TextBox58(self):
		self._getter_access_tracker["TextBox58"] = {}
		return self._TextBox58
	@TextBox58.setter
	def TextBox58(self, new_state):
		self._setter_access_tracker["TextBox58"] = {}
		global default_state
		self._TextBox58 = TextBox(new_state, default_state["TextBox58"])

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		global default_state
		self._TextBox46 = TextBox(new_state, default_state["TextBox46"])

	@property
	def TextBox64(self):
		self._getter_access_tracker["TextBox64"] = {}
		return self._TextBox64
	@TextBox64.setter
	def TextBox64(self, new_state):
		self._setter_access_tracker["TextBox64"] = {}
		global default_state
		self._TextBox64 = TextBox(new_state, default_state["TextBox64"])

	@property
	def TextBox65(self):
		self._getter_access_tracker["TextBox65"] = {}
		return self._TextBox65
	@TextBox65.setter
	def TextBox65(self, new_state):
		self._setter_access_tracker["TextBox65"] = {}
		global default_state
		self._TextBox65 = TextBox(new_state, default_state["TextBox65"])

	@property
	def TextBox66(self):
		self._getter_access_tracker["TextBox66"] = {}
		return self._TextBox66
	@TextBox66.setter
	def TextBox66(self, new_state):
		self._setter_access_tracker["TextBox66"] = {}
		global default_state
		self._TextBox66 = TextBox(new_state, default_state["TextBox66"])

	@property
	def Image24(self):
		self._getter_access_tracker["Image24"] = {}
		return self._Image24
	@Image24.setter
	def Image24(self, new_state):
		self._setter_access_tracker["Image24"] = {}
		global default_state
		self._Image24 = Image(new_state, default_state["Image24"])

	@property
	def TextBox73(self):
		self._getter_access_tracker["TextBox73"] = {}
		return self._TextBox73
	@TextBox73.setter
	def TextBox73(self, new_state):
		self._setter_access_tracker["TextBox73"] = {}
		global default_state
		self._TextBox73 = TextBox(new_state, default_state["TextBox73"])

	@property
	def TextBox74(self):
		self._getter_access_tracker["TextBox74"] = {}
		return self._TextBox74
	@TextBox74.setter
	def TextBox74(self, new_state):
		self._setter_access_tracker["TextBox74"] = {}
		global default_state
		self._TextBox74 = TextBox(new_state, default_state["TextBox74"])

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		global default_state
		self._TextBox75 = TextBox(new_state, default_state["TextBox75"])

	@property
	def Image25(self):
		self._getter_access_tracker["Image25"] = {}
		return self._Image25
	@Image25.setter
	def Image25(self, new_state):
		self._setter_access_tracker["Image25"] = {}
		global default_state
		self._Image25 = Image(new_state, default_state["Image25"])

	@property
	def TextBox77(self):
		self._getter_access_tracker["TextBox77"] = {}
		return self._TextBox77
	@TextBox77.setter
	def TextBox77(self, new_state):
		self._setter_access_tracker["TextBox77"] = {}
		global default_state
		self._TextBox77 = TextBox(new_state, default_state["TextBox77"])

	@property
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		global default_state
		self._TextBox79 = TextBox(new_state, default_state["TextBox79"])

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		global default_state
		self._TextBox80 = TextBox(new_state, default_state["TextBox80"])

	@property
	def Image26(self):
		self._getter_access_tracker["Image26"] = {}
		return self._Image26
	@Image26.setter
	def Image26(self, new_state):
		self._setter_access_tracker["Image26"] = {}
		global default_state
		self._Image26 = Image(new_state, default_state["Image26"])

	@property
	def TextBox81(self):
		self._getter_access_tracker["TextBox81"] = {}
		return self._TextBox81
	@TextBox81.setter
	def TextBox81(self, new_state):
		self._setter_access_tracker["TextBox81"] = {}
		global default_state
		self._TextBox81 = TextBox(new_state, default_state["TextBox81"])

	@property
	def TextBox82(self):
		self._getter_access_tracker["TextBox82"] = {}
		return self._TextBox82
	@TextBox82.setter
	def TextBox82(self, new_state):
		self._setter_access_tracker["TextBox82"] = {}
		global default_state
		self._TextBox82 = TextBox(new_state, default_state["TextBox82"])

	@property
	def TextBox83(self):
		self._getter_access_tracker["TextBox83"] = {}
		return self._TextBox83
	@TextBox83.setter
	def TextBox83(self, new_state):
		self._setter_access_tracker["TextBox83"] = {}
		global default_state
		self._TextBox83 = TextBox(new_state, default_state["TextBox83"])

	@property
	def Image27(self):
		self._getter_access_tracker["Image27"] = {}
		return self._Image27
	@Image27.setter
	def Image27(self, new_state):
		self._setter_access_tracker["Image27"] = {}
		global default_state
		self._Image27 = Image(new_state, default_state["Image27"])

	@property
	def TextBox84(self):
		self._getter_access_tracker["TextBox84"] = {}
		return self._TextBox84
	@TextBox84.setter
	def TextBox84(self, new_state):
		self._setter_access_tracker["TextBox84"] = {}
		global default_state
		self._TextBox84 = TextBox(new_state, default_state["TextBox84"])

	@property
	def TextBox85(self):
		self._getter_access_tracker["TextBox85"] = {}
		return self._TextBox85
	@TextBox85.setter
	def TextBox85(self, new_state):
		self._setter_access_tracker["TextBox85"] = {}
		global default_state
		self._TextBox85 = TextBox(new_state, default_state["TextBox85"])

	@property
	def TextBox86(self):
		self._getter_access_tracker["TextBox86"] = {}
		return self._TextBox86
	@TextBox86.setter
	def TextBox86(self, new_state):
		self._setter_access_tracker["TextBox86"] = {}
		global default_state
		self._TextBox86 = TextBox(new_state, default_state["TextBox86"])

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		global default_state
		self._Image28 = Image(new_state, default_state["Image28"])

	@property
	def TextBox87(self):
		self._getter_access_tracker["TextBox87"] = {}
		return self._TextBox87
	@TextBox87.setter
	def TextBox87(self, new_state):
		self._setter_access_tracker["TextBox87"] = {}
		global default_state
		self._TextBox87 = TextBox(new_state, default_state["TextBox87"])

	@property
	def TextBox88(self):
		self._getter_access_tracker["TextBox88"] = {}
		return self._TextBox88
	@TextBox88.setter
	def TextBox88(self, new_state):
		self._setter_access_tracker["TextBox88"] = {}
		global default_state
		self._TextBox88 = TextBox(new_state, default_state["TextBox88"])

	@property
	def TextBox89(self):
		self._getter_access_tracker["TextBox89"] = {}
		return self._TextBox89
	@TextBox89.setter
	def TextBox89(self, new_state):
		self._setter_access_tracker["TextBox89"] = {}
		global default_state
		self._TextBox89 = TextBox(new_state, default_state["TextBox89"])

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		global default_state
		self._Image29 = Image(new_state, default_state["Image29"])

	@property
	def TextBox91(self):
		self._getter_access_tracker["TextBox91"] = {}
		return self._TextBox91
	@TextBox91.setter
	def TextBox91(self, new_state):
		self._setter_access_tracker["TextBox91"] = {}
		global default_state
		self._TextBox91 = TextBox(new_state, default_state["TextBox91"])

	@property
	def TextBox90(self):
		self._getter_access_tracker["TextBox90"] = {}
		return self._TextBox90
	@TextBox90.setter
	def TextBox90(self, new_state):
		self._setter_access_tracker["TextBox90"] = {}
		global default_state
		self._TextBox90 = TextBox(new_state, default_state["TextBox90"])

	@property
	def TextBox93(self):
		self._getter_access_tracker["TextBox93"] = {}
		return self._TextBox93
	@TextBox93.setter
	def TextBox93(self, new_state):
		self._setter_access_tracker["TextBox93"] = {}
		global default_state
		self._TextBox93 = TextBox(new_state, default_state["TextBox93"])

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		global default_state
		self._Image31 = Image(new_state, default_state["Image31"])

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		global default_state
		self._Image30 = Image(new_state, default_state["Image30"])

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		global default_state
		self._Image33 = Image(new_state, default_state["Image33"])

	@property
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		global default_state
		self._Image32 = Image(new_state, default_state["Image32"])

	@property
	def TextBox97(self):
		self._getter_access_tracker["TextBox97"] = {}
		return self._TextBox97
	@TextBox97.setter
	def TextBox97(self, new_state):
		self._setter_access_tracker["TextBox97"] = {}
		global default_state
		self._TextBox97 = TextBox(new_state, default_state["TextBox97"])

	@property
	def TextBox96(self):
		self._getter_access_tracker["TextBox96"] = {}
		return self._TextBox96
	@TextBox96.setter
	def TextBox96(self, new_state):
		self._setter_access_tracker["TextBox96"] = {}
		global default_state
		self._TextBox96 = TextBox(new_state, default_state["TextBox96"])

	@property
	def TextBox98(self):
		self._getter_access_tracker["TextBox98"] = {}
		return self._TextBox98
	@TextBox98.setter
	def TextBox98(self, new_state):
		self._setter_access_tracker["TextBox98"] = {}
		global default_state
		self._TextBox98 = TextBox(new_state, default_state["TextBox98"])

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		global default_state
		self._Image36 = Image(new_state, default_state["Image36"])

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		global default_state
		self._Image34 = Image(new_state, default_state["Image34"])

	@property
	def TextBox94(self):
		self._getter_access_tracker["TextBox94"] = {}
		return self._TextBox94
	@TextBox94.setter
	def TextBox94(self, new_state):
		self._setter_access_tracker["TextBox94"] = {}
		global default_state
		self._TextBox94 = TextBox(new_state, default_state["TextBox94"])

	@property
	def TextBox101(self):
		self._getter_access_tracker["TextBox101"] = {}
		return self._TextBox101
	@TextBox101.setter
	def TextBox101(self, new_state):
		self._setter_access_tracker["TextBox101"] = {}
		global default_state
		self._TextBox101 = TextBox(new_state, default_state["TextBox101"])

	@property
	def TextBox102(self):
		self._getter_access_tracker["TextBox102"] = {}
		return self._TextBox102
	@TextBox102.setter
	def TextBox102(self, new_state):
		self._setter_access_tracker["TextBox102"] = {}
		global default_state
		self._TextBox102 = TextBox(new_state, default_state["TextBox102"])

	@property
	def Image39(self):
		self._getter_access_tracker["Image39"] = {}
		return self._Image39
	@Image39.setter
	def Image39(self, new_state):
		self._setter_access_tracker["Image39"] = {}
		global default_state
		self._Image39 = Image(new_state, default_state["Image39"])

	@property
	def TextBox105(self):
		self._getter_access_tracker["TextBox105"] = {}
		return self._TextBox105
	@TextBox105.setter
	def TextBox105(self, new_state):
		self._setter_access_tracker["TextBox105"] = {}
		global default_state
		self._TextBox105 = TextBox(new_state, default_state["TextBox105"])

	@property
	def TextBox108(self):
		self._getter_access_tracker["TextBox108"] = {}
		return self._TextBox108
	@TextBox108.setter
	def TextBox108(self, new_state):
		self._setter_access_tracker["TextBox108"] = {}
		global default_state
		self._TextBox108 = TextBox(new_state, default_state["TextBox108"])

	@property
	def TextBox109(self):
		self._getter_access_tracker["TextBox109"] = {}
		return self._TextBox109
	@TextBox109.setter
	def TextBox109(self, new_state):
		self._setter_access_tracker["TextBox109"] = {}
		global default_state
		self._TextBox109 = TextBox(new_state, default_state["TextBox109"])

	@property
	def TextBox110(self):
		self._getter_access_tracker["TextBox110"] = {}
		return self._TextBox110
	@TextBox110.setter
	def TextBox110(self, new_state):
		self._setter_access_tracker["TextBox110"] = {}
		global default_state
		self._TextBox110 = TextBox(new_state, default_state["TextBox110"])

	@property
	def Image40(self):
		self._getter_access_tracker["Image40"] = {}
		return self._Image40
	@Image40.setter
	def Image40(self, new_state):
		self._setter_access_tracker["Image40"] = {}
		global default_state
		self._Image40 = Image(new_state, default_state["Image40"])

	@property
	def Image45(self):
		self._getter_access_tracker["Image45"] = {}
		return self._Image45
	@Image45.setter
	def Image45(self, new_state):
		self._setter_access_tracker["Image45"] = {}
		global default_state
		self._Image45 = Image(new_state, default_state["Image45"])

	@property
	def TextBox121(self):
		self._getter_access_tracker["TextBox121"] = {}
		return self._TextBox121
	@TextBox121.setter
	def TextBox121(self, new_state):
		self._setter_access_tracker["TextBox121"] = {}
		global default_state
		self._TextBox121 = TextBox(new_state, default_state["TextBox121"])

	@property
	def TextBox122(self):
		self._getter_access_tracker["TextBox122"] = {}
		return self._TextBox122
	@TextBox122.setter
	def TextBox122(self, new_state):
		self._setter_access_tracker["TextBox122"] = {}
		global default_state
		self._TextBox122 = TextBox(new_state, default_state["TextBox122"])

	@property
	def TextBox123(self):
		self._getter_access_tracker["TextBox123"] = {}
		return self._TextBox123
	@TextBox123.setter
	def TextBox123(self, new_state):
		self._setter_access_tracker["TextBox123"] = {}
		global default_state
		self._TextBox123 = TextBox(new_state, default_state["TextBox123"])

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		global default_state
		self._Image35 = Image(new_state, default_state["Image35"])

	@property
	def TextBox95(self):
		self._getter_access_tracker["TextBox95"] = {}
		return self._TextBox95
	@TextBox95.setter
	def TextBox95(self, new_state):
		self._setter_access_tracker["TextBox95"] = {}
		global default_state
		self._TextBox95 = TextBox(new_state, default_state["TextBox95"])

	@property
	def TextBox133(self):
		self._getter_access_tracker["TextBox133"] = {}
		return self._TextBox133
	@TextBox133.setter
	def TextBox133(self, new_state):
		self._setter_access_tracker["TextBox133"] = {}
		global default_state
		self._TextBox133 = TextBox(new_state, default_state["TextBox133"])

	@property
	def TextBox134(self):
		self._getter_access_tracker["TextBox134"] = {}
		return self._TextBox134
	@TextBox134.setter
	def TextBox134(self, new_state):
		self._setter_access_tracker["TextBox134"] = {}
		global default_state
		self._TextBox134 = TextBox(new_state, default_state["TextBox134"])

	@property
	def TextBox135(self):
		self._getter_access_tracker["TextBox135"] = {}
		return self._TextBox135
	@TextBox135.setter
	def TextBox135(self, new_state):
		self._setter_access_tracker["TextBox135"] = {}
		global default_state
		self._TextBox135 = TextBox(new_state, default_state["TextBox135"])

	@property
	def Image49(self):
		self._getter_access_tracker["Image49"] = {}
		return self._Image49
	@Image49.setter
	def Image49(self, new_state):
		self._setter_access_tracker["Image49"] = {}
		global default_state
		self._Image49 = Image(new_state, default_state["Image49"])

	@property
	def TextBox136(self):
		self._getter_access_tracker["TextBox136"] = {}
		return self._TextBox136
	@TextBox136.setter
	def TextBox136(self, new_state):
		self._setter_access_tracker["TextBox136"] = {}
		global default_state
		self._TextBox136 = TextBox(new_state, default_state["TextBox136"])

	@property
	def TextBox137(self):
		self._getter_access_tracker["TextBox137"] = {}
		return self._TextBox137
	@TextBox137.setter
	def TextBox137(self, new_state):
		self._setter_access_tracker["TextBox137"] = {}
		global default_state
		self._TextBox137 = TextBox(new_state, default_state["TextBox137"])

	@property
	def TextBox138(self):
		self._getter_access_tracker["TextBox138"] = {}
		return self._TextBox138
	@TextBox138.setter
	def TextBox138(self, new_state):
		self._setter_access_tracker["TextBox138"] = {}
		global default_state
		self._TextBox138 = TextBox(new_state, default_state["TextBox138"])

	@property
	def Image50(self):
		self._getter_access_tracker["Image50"] = {}
		return self._Image50
	@Image50.setter
	def Image50(self, new_state):
		self._setter_access_tracker["Image50"] = {}
		global default_state
		self._Image50 = Image(new_state, default_state["Image50"])

	@property
	def TextBox142(self):
		self._getter_access_tracker["TextBox142"] = {}
		return self._TextBox142
	@TextBox142.setter
	def TextBox142(self, new_state):
		self._setter_access_tracker["TextBox142"] = {}
		global default_state
		self._TextBox142 = TextBox(new_state, default_state["TextBox142"])

	@property
	def TextBox143(self):
		self._getter_access_tracker["TextBox143"] = {}
		return self._TextBox143
	@TextBox143.setter
	def TextBox143(self, new_state):
		self._setter_access_tracker["TextBox143"] = {}
		global default_state
		self._TextBox143 = TextBox(new_state, default_state["TextBox143"])

	@property
	def Image51(self):
		self._getter_access_tracker["Image51"] = {}
		return self._Image51
	@Image51.setter
	def Image51(self, new_state):
		self._setter_access_tracker["Image51"] = {}
		global default_state
		self._Image51 = Image(new_state, default_state["Image51"])

	@property
	def TextBox141(self):
		self._getter_access_tracker["TextBox141"] = {}
		return self._TextBox141
	@TextBox141.setter
	def TextBox141(self, new_state):
		self._setter_access_tracker["TextBox141"] = {}
		global default_state
		self._TextBox141 = TextBox(new_state, default_state["TextBox141"])

	@property
	def Image52(self):
		self._getter_access_tracker["Image52"] = {}
		return self._Image52
	@Image52.setter
	def Image52(self, new_state):
		self._setter_access_tracker["Image52"] = {}
		global default_state
		self._Image52 = Image(new_state, default_state["Image52"])

	@property
	def TextBox139(self):
		self._getter_access_tracker["TextBox139"] = {}
		return self._TextBox139
	@TextBox139.setter
	def TextBox139(self, new_state):
		self._setter_access_tracker["TextBox139"] = {}
		global default_state
		self._TextBox139 = TextBox(new_state, default_state["TextBox139"])

	@property
	def TextBox140(self):
		self._getter_access_tracker["TextBox140"] = {}
		return self._TextBox140
	@TextBox140.setter
	def TextBox140(self, new_state):
		self._setter_access_tracker["TextBox140"] = {}
		global default_state
		self._TextBox140 = TextBox(new_state, default_state["TextBox140"])

	@property
	def TextBox144(self):
		self._getter_access_tracker["TextBox144"] = {}
		return self._TextBox144
	@TextBox144.setter
	def TextBox144(self, new_state):
		self._setter_access_tracker["TextBox144"] = {}
		global default_state
		self._TextBox144 = TextBox(new_state, default_state["TextBox144"])

	@property
	def TextBox145(self):
		self._getter_access_tracker["TextBox145"] = {}
		return self._TextBox145
	@TextBox145.setter
	def TextBox145(self, new_state):
		self._setter_access_tracker["TextBox145"] = {}
		global default_state
		self._TextBox145 = TextBox(new_state, default_state["TextBox145"])

	@property
	def TextBox168(self):
		self._getter_access_tracker["TextBox168"] = {}
		return self._TextBox168
	@TextBox168.setter
	def TextBox168(self, new_state):
		self._setter_access_tracker["TextBox168"] = {}
		global default_state
		self._TextBox168 = TextBox(new_state, default_state["TextBox168"])

	@property
	def TextBox169(self):
		self._getter_access_tracker["TextBox169"] = {}
		return self._TextBox169
	@TextBox169.setter
	def TextBox169(self, new_state):
		self._setter_access_tracker["TextBox169"] = {}
		global default_state
		self._TextBox169 = TextBox(new_state, default_state["TextBox169"])

	@property
	def TextBox162(self):
		self._getter_access_tracker["TextBox162"] = {}
		return self._TextBox162
	@TextBox162.setter
	def TextBox162(self, new_state):
		self._setter_access_tracker["TextBox162"] = {}
		global default_state
		self._TextBox162 = TextBox(new_state, default_state["TextBox162"])

	@property
	def TextBox163(self):
		self._getter_access_tracker["TextBox163"] = {}
		return self._TextBox163
	@TextBox163.setter
	def TextBox163(self, new_state):
		self._setter_access_tracker["TextBox163"] = {}
		global default_state
		self._TextBox163 = TextBox(new_state, default_state["TextBox163"])

	@property
	def TextBox160(self):
		self._getter_access_tracker["TextBox160"] = {}
		return self._TextBox160
	@TextBox160.setter
	def TextBox160(self, new_state):
		self._setter_access_tracker["TextBox160"] = {}
		global default_state
		self._TextBox160 = TextBox(new_state, default_state["TextBox160"])

	@property
	def TextBox161(self):
		self._getter_access_tracker["TextBox161"] = {}
		return self._TextBox161
	@TextBox161.setter
	def TextBox161(self, new_state):
		self._setter_access_tracker["TextBox161"] = {}
		global default_state
		self._TextBox161 = TextBox(new_state, default_state["TextBox161"])

	@property
	def TextBox164(self):
		self._getter_access_tracker["TextBox164"] = {}
		return self._TextBox164
	@TextBox164.setter
	def TextBox164(self, new_state):
		self._setter_access_tracker["TextBox164"] = {}
		global default_state
		self._TextBox164 = TextBox(new_state, default_state["TextBox164"])

	@property
	def TextBox165(self):
		self._getter_access_tracker["TextBox165"] = {}
		return self._TextBox165
	@TextBox165.setter
	def TextBox165(self, new_state):
		self._setter_access_tracker["TextBox165"] = {}
		global default_state
		self._TextBox165 = TextBox(new_state, default_state["TextBox165"])

	@property
	def TextBox176(self):
		self._getter_access_tracker["TextBox176"] = {}
		return self._TextBox176
	@TextBox176.setter
	def TextBox176(self, new_state):
		self._setter_access_tracker["TextBox176"] = {}
		global default_state
		self._TextBox176 = TextBox(new_state, default_state["TextBox176"])

	@property
	def TextBox178(self):
		self._getter_access_tracker["TextBox178"] = {}
		return self._TextBox178
	@TextBox178.setter
	def TextBox178(self, new_state):
		self._setter_access_tracker["TextBox178"] = {}
		global default_state
		self._TextBox178 = TextBox(new_state, default_state["TextBox178"])

	@property
	def TextBox177(self):
		self._getter_access_tracker["TextBox177"] = {}
		return self._TextBox177
	@TextBox177.setter
	def TextBox177(self, new_state):
		self._setter_access_tracker["TextBox177"] = {}
		global default_state
		self._TextBox177 = TextBox(new_state, default_state["TextBox177"])

	@property
	def TextBox181(self):
		self._getter_access_tracker["TextBox181"] = {}
		return self._TextBox181
	@TextBox181.setter
	def TextBox181(self, new_state):
		self._setter_access_tracker["TextBox181"] = {}
		global default_state
		self._TextBox181 = TextBox(new_state, default_state["TextBox181"])

	@property
	def TextBox179(self):
		self._getter_access_tracker["TextBox179"] = {}
		return self._TextBox179
	@TextBox179.setter
	def TextBox179(self, new_state):
		self._setter_access_tracker["TextBox179"] = {}
		global default_state
		self._TextBox179 = TextBox(new_state, default_state["TextBox179"])

	@property
	def TextBox180(self):
		self._getter_access_tracker["TextBox180"] = {}
		return self._TextBox180
	@TextBox180.setter
	def TextBox180(self, new_state):
		self._setter_access_tracker["TextBox180"] = {}
		global default_state
		self._TextBox180 = TextBox(new_state, default_state["TextBox180"])

	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"Div6": self._Div6,
			"Flex13": self._Flex13,
			"Flex16": self._Flex16,
			"Flex17": self._Flex17,
			"Flex18": self._Flex18,
			"Flex19": self._Flex19,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"Flex23": self._Flex23,
			"Flex25": self._Flex25,
			"Flex26": self._Flex26,
			"Flex9": self._Flex9,
			"Flex32": self._Flex32,
			"Flex40": self._Flex40,
			"Flex41": self._Flex41,
			"Flex45": self._Flex45,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"Flex48": self._Flex48,
			"Flex33": self._Flex33,
			"Flex35": self._Flex35,
			"Flex36": self._Flex36,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"Flex39": self._Flex39,
			"Flex55": self._Flex55,
			"Flex56": self._Flex56,
			"Flex61": self._Flex61,
			"Flex57": self._Flex57,
			"Flex58": self._Flex58,
			"Flex64": self._Flex64,
			"Flex67": self._Flex67,
			"Flex68": self._Flex68,
			"Flex85": self._Flex85,
			"Flex86": self._Flex86,
			"Flex87": self._Flex87,
			"Flex62": self._Flex62,
			"Flex71": self._Flex71,
			"Flex88": self._Flex88,
			"Flex93": self._Flex93,
			"Flex94": self._Flex94,
			"Flex100": self._Flex100,
			"Flex74": self._Flex74,
			"Flex76": self._Flex76,
			"Flex79": self._Flex79,
			"Flex83": self._Flex83,
			"Flex84": self._Flex84,
			"Flex89": self._Flex89,
			"Flex90": self._Flex90,
			"Flex91": self._Flex91,
			"Flex60": self._Flex60,
			"Flex101": self._Flex101,
			"Flex102": self._Flex102,
			"Flex104": self._Flex104,
			"Flex105": self._Flex105,
			"Flex106": self._Flex106,
			"Flex107": self._Flex107,
			"Flex103": self._Flex103,
			"Flex108": self._Flex108,
			"Flex113": self._Flex113,
			"Flex109": self._Flex109,
			"Flex114": self._Flex114,
			"Flex115": self._Flex115,
			"Flex116": self._Flex116,
			"Flex110": self._Flex110,
			"Flex117": self._Flex117,
			"Flex118": self._Flex118,
			"Flex119": self._Flex119,
			"Flex111": self._Flex111,
			"Flex120": self._Flex120,
			"Flex121": self._Flex121,
			"Flex122": self._Flex122,
			"Flex112": self._Flex112,
			"Flex123": self._Flex123,
			"Flex124": self._Flex124,
			"Flex125": self._Flex125,
			"Flex129": self._Flex129,
			"Flex128": self._Flex128,
			"Flex132": self._Flex132,
			"Flex133": self._Flex133,
			"Flex130": self._Flex130,
			"Flex134": self._Flex134,
			"Flex135": self._Flex135,
			"Flex137": self._Flex137,
			"Flex138": self._Flex138,
			"Flex136": self._Flex136,
			"Flex139": self._Flex139,
			"Flex140": self._Flex140,
			"Flex143": self._Flex143,
			"Flex144": self._Flex144,
			"Flex146": self._Flex146,
			"Flex158": self._Flex158,
			"Flex164": self._Flex164,
			"Flex165": self._Flex165,
			"Flex159": self._Flex159,
			"Flex166": self._Flex166,
			"Flex167": self._Flex167,
			"Flex147": self._Flex147,
			"Flex154": self._Flex154,
			"Flex155": self._Flex155,
			"Flex148": self._Flex148,
			"Flex160": self._Flex160,
			"Flex173": self._Flex173,
			"Flex171": self._Flex171,
			"Flex172": self._Flex172,
			"Flex149": self._Flex149,
			"Flex162": self._Flex162,
			"Flex176": self._Flex176,
			"Flex174": self._Flex174,
			"Flex175": self._Flex175,
			"Flex145": self._Flex145,
			"Flex152": self._Flex152,
			"Flex204": self._Flex204,
			"Flex202": self._Flex202,
			"Flex198": self._Flex198,
			"Flex199": self._Flex199,
			"Flex203": self._Flex203,
			"Flex200": self._Flex200,
			"Flex201": self._Flex201,
			"Flex153": self._Flex153,
			"Flex156": self._Flex156,
			"Flex157": self._Flex157,
			"Flex232": self._Flex232,
			"Flex230": self._Flex230,
			"Flex226": self._Flex226,
			"Flex227": self._Flex227,
			"Flex231": self._Flex231,
			"Flex228": self._Flex228,
			"Flex229": self._Flex229,
			"Flex239": self._Flex239,
			"Flex237": self._Flex237,
			"Flex233": self._Flex233,
			"Flex234": self._Flex234,
			"Flex238": self._Flex238,
			"Flex235": self._Flex235,
			"Flex236": self._Flex236,
			"Flex240": self._Flex240,
			"Flex245": self._Flex245,
			"Flex246": self._Flex246,
			"Flex249": self._Flex249,
			"Flex252": self._Flex252,
			"Flex248": self._Flex248,
			"Flex244": self._Flex244,
			"Flex241": self._Flex241,
			"Flex242": self._Flex242,
			"Flex243": self._Flex243,
			"Flex253": self._Flex253,
			"Flex254": self._Flex254,
			"Flex255": self._Flex255,
			"Flex256": self._Flex256,
			"Flex257": self._Flex257,
			"Flex278": self._Flex278,
			"Flex280": self._Flex280,
			"Flex281": self._Flex281,
			"Flex258": self._Flex258,
			"Flex263": self._Flex263,
			"Flex274": self._Flex274,
			"Flex279": self._Flex279,
			"Flex282": self._Flex282,
			"Flex283": self._Flex283,
			"Flex296": self._Flex296,
			"Flex293": self._Flex293,
			"Flex295": self._Flex295,
			"Flex294": self._Flex294,
			"Flex297": self._Flex297,
			"Flex292": self._Flex292,
			"Flex291": self._Flex291,
			"TextBox1": self._TextBox1,
			"TextBox17": self._TextBox17,
			"TextBox20": self._TextBox20,
			"TextBox19": self._TextBox19,
			"TextBox18": self._TextBox18,
			"TextBox22": self._TextBox22,
			"Image3": self._Image3,
			"TextBox23": self._TextBox23,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"Button4": self._Button4,
			"Button6": self._Button6,
			"Image1": self._Image1,
			"TextBox29": self._TextBox29,
			"TextBox31": self._TextBox31,
			"Image9": self._Image9,
			"TextBox33": self._TextBox33,
			"TextBox37": self._TextBox37,
			"Image12": self._Image12,
			"Image10": self._Image10,
			"TextBox34": self._TextBox34,
			"TextBox38": self._TextBox38,
			"Image13": self._Image13,
			"Image11": self._Image11,
			"TextBox36": self._TextBox36,
			"TextBox39": self._TextBox39,
			"Image14": self._Image14,
			"TextBox28": self._TextBox28,
			"Image5": self._Image5,
			"Image6": self._Image6,
			"Image7": self._Image7,
			"Image8": self._Image8,
			"TextBox48": self._TextBox48,
			"Button7": self._Button7,
			"Image16": self._Image16,
			"TextBox50": self._TextBox50,
			"TextBox51": self._TextBox51,
			"TextBox52": self._TextBox52,
			"Image19": self._Image19,
			"Image17": self._Image17,
			"TextBox54": self._TextBox54,
			"TextBox59": self._TextBox59,
			"TextBox53": self._TextBox53,
			"TextBox62": self._TextBox62,
			"Image22": self._Image22,
			"Image18": self._Image18,
			"TextBox56": self._TextBox56,
			"TextBox55": self._TextBox55,
			"Image21": self._Image21,
			"TextBox57": self._TextBox57,
			"TextBox58": self._TextBox58,
			"TextBox46": self._TextBox46,
			"TextBox64": self._TextBox64,
			"TextBox65": self._TextBox65,
			"TextBox66": self._TextBox66,
			"Image24": self._Image24,
			"TextBox73": self._TextBox73,
			"TextBox74": self._TextBox74,
			"TextBox75": self._TextBox75,
			"Image25": self._Image25,
			"TextBox77": self._TextBox77,
			"TextBox79": self._TextBox79,
			"TextBox80": self._TextBox80,
			"Image26": self._Image26,
			"TextBox81": self._TextBox81,
			"TextBox82": self._TextBox82,
			"TextBox83": self._TextBox83,
			"Image27": self._Image27,
			"TextBox84": self._TextBox84,
			"TextBox85": self._TextBox85,
			"TextBox86": self._TextBox86,
			"Image28": self._Image28,
			"TextBox87": self._TextBox87,
			"TextBox88": self._TextBox88,
			"TextBox89": self._TextBox89,
			"Image29": self._Image29,
			"TextBox91": self._TextBox91,
			"TextBox90": self._TextBox90,
			"TextBox93": self._TextBox93,
			"Image31": self._Image31,
			"Image30": self._Image30,
			"Image33": self._Image33,
			"Image32": self._Image32,
			"TextBox97": self._TextBox97,
			"TextBox96": self._TextBox96,
			"TextBox98": self._TextBox98,
			"Image36": self._Image36,
			"Image34": self._Image34,
			"TextBox94": self._TextBox94,
			"TextBox101": self._TextBox101,
			"TextBox102": self._TextBox102,
			"Image39": self._Image39,
			"TextBox105": self._TextBox105,
			"TextBox108": self._TextBox108,
			"TextBox109": self._TextBox109,
			"TextBox110": self._TextBox110,
			"Image40": self._Image40,
			"Image45": self._Image45,
			"TextBox121": self._TextBox121,
			"TextBox122": self._TextBox122,
			"TextBox123": self._TextBox123,
			"Image35": self._Image35,
			"TextBox95": self._TextBox95,
			"TextBox133": self._TextBox133,
			"TextBox134": self._TextBox134,
			"TextBox135": self._TextBox135,
			"Image49": self._Image49,
			"TextBox136": self._TextBox136,
			"TextBox137": self._TextBox137,
			"TextBox138": self._TextBox138,
			"Image50": self._Image50,
			"TextBox142": self._TextBox142,
			"TextBox143": self._TextBox143,
			"Image51": self._Image51,
			"TextBox141": self._TextBox141,
			"Image52": self._Image52,
			"TextBox139": self._TextBox139,
			"TextBox140": self._TextBox140,
			"TextBox144": self._TextBox144,
			"TextBox145": self._TextBox145,
			"TextBox168": self._TextBox168,
			"TextBox169": self._TextBox169,
			"TextBox162": self._TextBox162,
			"TextBox163": self._TextBox163,
			"TextBox160": self._TextBox160,
			"TextBox161": self._TextBox161,
			"TextBox164": self._TextBox164,
			"TextBox165": self._TextBox165,
			"TextBox176": self._TextBox176,
			"TextBox178": self._TextBox178,
			"TextBox177": self._TextBox177,
			"TextBox181": self._TextBox181,
			"TextBox179": self._TextBox179,
			"TextBox180": self._TextBox180,
			}


class FlexstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.flexDirection: str = get_defined_value(state, def_state, "flexDirection")
		self.alignItems: str = get_defined_value(state, def_state, "alignItems")
		self.justifyContent: str = get_defined_value(state, def_state, "justifyContent")
		self.flexWrap: str = get_defined_value(state, def_state, "flexWrap")
		self.alignContent: str = get_defined_value(state, def_state, "alignContent")
		self.rowGap: str = get_defined_value(state, def_state, "rowGap")
		self.columnGap: str = get_defined_value(state, def_state, "columnGap")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def flexDirection(self):
		self._getter_access_tracker["flexDirection"] = {}
		return self._flexDirection
	@flexDirection.setter
	def flexDirection(self, state):
		self._setter_access_tracker["flexDirection"] = {}
		self._flexDirection = state
	@property
	def alignItems(self):
		self._getter_access_tracker["alignItems"] = {}
		return self._alignItems
	@alignItems.setter
	def alignItems(self, state):
		self._setter_access_tracker["alignItems"] = {}
		self._alignItems = state
	@property
	def justifyContent(self):
		self._getter_access_tracker["justifyContent"] = {}
		return self._justifyContent
	@justifyContent.setter
	def justifyContent(self, state):
		self._setter_access_tracker["justifyContent"] = {}
		self._justifyContent = state
	@property
	def flexWrap(self):
		self._getter_access_tracker["flexWrap"] = {}
		return self._flexWrap
	@flexWrap.setter
	def flexWrap(self, state):
		self._setter_access_tracker["flexWrap"] = {}
		self._flexWrap = state
	@property
	def alignContent(self):
		self._getter_access_tracker["alignContent"] = {}
		return self._alignContent
	@alignContent.setter
	def alignContent(self, state):
		self._setter_access_tracker["alignContent"] = {}
		self._alignContent = state
	@property
	def rowGap(self):
		self._getter_access_tracker["rowGap"] = {}
		return self._rowGap
	@rowGap.setter
	def rowGap(self, state):
		self._setter_access_tracker["rowGap"] = {}
		self._rowGap = state
	@property
	def columnGap(self):
		self._getter_access_tracker["columnGap"] = {}
		return self._columnGap
	@columnGap.setter
	def columnGap(self, state):
		self._setter_access_tracker["columnGap"] = {}
		self._columnGap = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"flexDirection": self._flexDirection,
			"alignItems": self._alignItems,
			"justifyContent": self._justifyContent,
			"flexWrap": self._flexWrap,
			"alignContent": self._alignContent,
			"rowGap": self._rowGap,
			"columnGap": self._columnGap,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Flex:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: FlexstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = FlexstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class DivstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Div:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: DivstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = DivstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class TextBoxstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class TextBoxcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class TextBox:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: TextBoxstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: TextBoxcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = TextBoxstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = TextBoxcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ImagestylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ImagecustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alt: str = get_defined_value(state, def_state, "alt")
		self.src: str = get_defined_value(state, def_state, "src")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alt(self):
		self._getter_access_tracker["alt"] = {}
		return self._alt
	@alt.setter
	def alt(self, state):
		self._setter_access_tracker["alt"] = {}
		self._alt = state
	@property
	def src(self):
		self._getter_access_tracker["src"] = {}
		return self._src
	@src.setter
	def src(self, state):
		self._setter_access_tracker["src"] = {}
		self._src = state
	def _to_json_fields(self):
		return {
			"alt": self._alt,
			"src": self._src,
			}


class Image:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ImagestylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ImagecustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ImagestylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ImagecustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ButtonstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ButtoncustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class Button:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ButtonstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ButtoncustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ButtonstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ButtoncustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

