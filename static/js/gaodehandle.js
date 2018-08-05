$(function () { // 加载完成DOM立即执行

    var map = new AMap.Map("container", {
        resizeEnable: true
    });

    var cpoint = new AMap.LngLat(116.39739, 39.90886);

    $('#getStationLngLat').click(function () {
        searchLngLat();
    })

<<<<<<< HEAD
=======
    $('#getgateway').click(function () {
        var stations = getStationName();
        stations.forEach(function (cur) {
            searchGateway(cur);
        })
    })

>>>>>>> 备注

    $('#getPoi').click(function () {

        var stationdetail = getStationDetail();
        if (stationdetail) {
            console.log('车站数据读取成功')
        }
        var tags = getTagInfo();
        if (tags) {
            console.log("标签信息读入成功")
        }

        stationdetail.forEach(function (cur) {
            transition(cur, tags);
        })
    });

    function searchLngLat() {
        AMap.service(["AMap.PlaceSearch"], function () {
            for (var i = 0; i < 9; i++) {
                var placeSearch = new AMap.PlaceSearch({ //构造地点查询类
                    pageSize: 50,
                    pageIndex: i + 1,
                    city: "010", //城市
                    map: map,
                    panel: "panel"
                });
                //关键字查询
                placeSearch.search('地铁站', function (status, result) {
                    console.log(result.poiList.count);
                    var distances = new Array();
                    result.poiList.pois.forEach(function (curPoi) {
                        distances.push(cpoint.distance(curPoi.location));
                    })
                    sendStationData(result.poiList.pois, distances);
                });
            }
        });
    }

<<<<<<< HEAD
=======
    function searchGateway(curSta) {
        AMap.service(["AMap.PlaceSearch"], function () {
            var placeSearch = new AMap.PlaceSearch({
                pageSize: 10,
                pageIndex: 1,
                city: "010",
                map: map,
                type: 150501,
                panel: "panel"
            });

            placeSearch.search(curSta, function (status, result) {
                console.log(result);
                var distances = new Array();
                result.poiList.pois.forEach(function (curPoi) {
                    distances.push(cpoint.distance(curPoi.location));
                })
                sendGateway(result.poiList, distances)
            })
        })
    }

>>>>>>> 备注
    function searchPoi(curSta, curTag, pageIndex) {   //对车站按tag进行搜索
        AMap.service(["AMap.PlaceSearch"], function () {
            var placeSearch = new AMap.PlaceSearch({ //构造地点查询类
                pageSize: 50,
                type: curTag.name,
                pageIndex: pageIndex,
                city: "010",//城市
                map: map,
                panel: "panel",
<<<<<<< HEAD
                autoFitView:false
=======
                autoFitView: false
>>>>>>> 备注
            });


            var cpoint = new AMap.LngLat(curSta.point.lng, curSta.point.lat);
            placeSearch.searchNearBy('', cpoint, 2000, function (status, result) {
                if (result.info === 'OK') {
                    sendPoiDetail(curSta.id, curTag.id, result.poiList.pois);
<<<<<<< HEAD
                    console.log('对%s的所有%s标签搜索完成!', curSta.name,curTag.name);
=======
                    console.log('对%s的所有%s标签搜索完成!', curSta.name, curTag.name);
>>>>>>> 备注
                    if (curTag.name === '虚拟门') {
                        console.log('对%s的所有标签搜索完成!!!', curSta.name);
                    }
                }
            });
        })
    }

    function sendStationData(data, distances) {
        $.ajax({
            type: "POST",
            url: "/saveStation",
            async: false,
            data: JSON.stringify({'data': data, 'distance': distances}),
            contentType: "application/json",
            dataType: "json",
            complete: function (msg) {
                if (msg.status === 404) {
                }
            }
        })
    }

    function sendPoiDetail(curStaId, curTagId, data) {    //将搜索的Poi信息发到后台保存
        $.ajax({
            type: "POST",
            url: "/savePoi",
            async: false,
            data: JSON.stringify({'staId': curStaId, 'tagId': curTagId, 'data': data}),
            contentType: "application/json",
            dataType: "json",
            complete: function (msg) {
                if (msg.status === 404) {
                }
            }
        });
    }

<<<<<<< HEAD
=======
    function sendGateway(data, distances) {
        $.ajax({
            type: "POST",
            url: "/saveGateway",
            async: false,
            data: JSON.stringify({'data': data, 'distance': distances}),
            contentType: "application/json",
            dataType: "json",
            complete: function (msg) {
                if (msg.status === 404) {
                }
            }
        })
    }

>>>>>>> 备注
    function transition(cur, tags) {     //过渡函数
        tags.forEach(function (curtag) {
            for (var i = 0; i < 4; i++) {
                searchPoi(cur, curtag, i + 1);
            }
        });
    }

    function getStationDetail() {      //从后台读取车站及其经纬度信息
        var rsp;
        $.ajax({
            type: "GET",
            url: "/stationDetail",
            async: false,
            success: function (result) {
                if (result.status !== 200) return;
                rsp = result.data;
            }
        });
        return rsp;
    }

<<<<<<< HEAD
=======
    function getStationName() {
        var rsp;
        $.ajax({
            type: "GET",
            url: "/stationName",
            async: false,
            success: function (result) {
                if (result.status != 200) return;
                rsp = result.data;
            }
        });
        return rsp;
    }

>>>>>>> 备注
    function getTagInfo() {            //从后台读取tag信息
        var rsp;
        $.ajax({
            type: "GET",
            url: "/stationPOITag",
            async: false,
            success: function (result) {
                if (result.status !== 200) return;
                rsp = result.data;
            }
        });
        return rsp;
    }
})
