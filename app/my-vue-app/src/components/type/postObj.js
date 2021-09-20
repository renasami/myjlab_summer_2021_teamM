export function postObj(id,uid,title,caption,url,likedNumber){
    this.id = id;
    this.uid = uid;
    this.title = title;
    this.samb = `${url.replace("https://www.youtube.com/embed/","https://img.youtube.com/vi/")}/maxresdefault.jpg`
    this.caption = caption;
    this.url = url;
    this.likedNumber = likedNumber;
    this.isLike = false;
    this.comment = []
  }