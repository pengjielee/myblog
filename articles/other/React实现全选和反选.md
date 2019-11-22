## CheckboxList.js
~~~
class CheckboxList extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      data: [
        { 'name':'red', 'checked': true },
        { 'name':'green', 'checked': false },
        { 'name':'blue', 'checked': false }
      ],
      checkedAll: false, //全选状态
      checkedInvert: false //反选状态
    }
    this.handleAllChange = this.handleAllChange.bind(this);
    this.handleInvertChange = this.handleInvertChange.bind(this);
    this.handleItemChange = this.handleItemChange.bind(this);
  }

  // 全选事件
  handleAllChange(){
    const { checkedAll,data } = this.state;

    data.map(function(item,index){
      return item.checked = !checkedAll;
    })

    this.setState({
      checkedAll: !checkedAll,
      checkedInvert: false,
      data: data
    });
  }

  // 反选事件
  handleInvertChange(){
    const { checkedInvert, data } = this.state;

    data.map(function(item,index){
      return item.checked = !item.checked;
    })

    const checkedAll = data.every(function(item,index){
      return item.checked;
    })

    this.setState({
      checkedAll: checkedAll,
      checkedInvert: !checkedInvert,
      data: data
    });
  }

  // CheckItem事件
  handleItemChange(ckitem){
    const data = this.state.data;
    const checked = ckitem.checked;
    let checkedInvert = this.state.checkedInvert;

    data.map(function(item,index){
      if(item.name === ckitem.name){
        return item.checked = ckitem.checked
      }
    })

    const checkedAll = data.every(function(item,index){
      return item.checked;
    })

    checkedInvert = checkedAll ? false : checkedInvert;

    this.setState({
      data: data,
      checkedAll: checkedAll,
      checkedInvert: checkedInvert
    })
  }

  renderList(){
    var that = this;
    return this.state.data.map(function(item,index){
      return <CheckboxItem {...item} key={index} handleItemChange={that.handleItemChange}/>
    })
  }

  render(){
    const {checkedAll,checkedInvert} = this.state
    return(
      <div className="container">
        <div className="checkbox-control">
          <label><input type="checkbox" checked={checkedAll} onChange={ this.handleAllChange }/>全选</label>
          <label><input type="checkbox" checked={checkedInvert} onChange={ this.handleInvertChange }/>反选</label>
        </div>
        <div className="checkbox-list">
          {this.renderList()}
        </div>
      </div>
    ) 
  }
}
~~~

## CheckboxItem.js
~~~
class CheckboxItem extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      checked: props.checked,
      name: props.name
    }
    this.handleChange = this.handleChange.bind(this);
  }

  componentWillReceiveProps(nextProps,prevProps){
    if(nextProps.checked != prevProps.checked){
      this.setState({
        checked: nextProps.checked
      })
    }
  }

  handleChange(){
    const { checked,name } = this.state
    this.setState({
      checked: !checked
    },function(){
      this.props.handleItemChange({ name: name, checked: !checked });
    })
  }

  render(){
    const {checked,name} = this.state
    return(
      <div>
        <label className="checkbox-item"><input type="checkbox" checked={checked} onChange={ this.handleChange }/>{name}</label>
      </div>
    )
  }
}
~~~

## App.js
~~~
ReactDOM.render(
  <CheckboxList />,
  document.getElementById('root')
);
~~~

[预览效果](http://m.pengjielee.cn/checkall.html)  
http://m.pengjielee.cn/checkall.html
