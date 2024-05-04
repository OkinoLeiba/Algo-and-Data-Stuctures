class DynamicArray {
    constructor(values) {
        this.values = values | null;
        this.sizeOfArray = this.sizeOfArrayGetter - 1;
        this.lenOfArray = this.sizeOfArrayGetter;
        this.thisDynArray = null;
    }

    // dynArray1 = new Array(5);
    // dynArray1.apply(this, Array(5)).map(() => {})

    // test = () => {
    //     console.log(this.sizeOfArray);
    // }

    createArray = function() {
        var value = 10;
        var dynArray = new Array(value);
        // for (var i = 0; i < 10; i++) {
        //     dynArray[i] = i;
        //     this.sizeOfArray += 1
        // };
        // dynArray.fill(value, 0 , 10);
        // dynArray.map((value) => (new Array(value).fill(value, 0 , value)));
        // dynArray.map(value => value--).sort();

        dynArray.fill().map(() => {return Math.floor(Math.random() * value)});

        this.thisDynArray = Array(value).fill().map(() => Math.floor(Math.random() * value));   
        
    }

    resizeArray() {
        this.lenOfArray = this.sizeOfArrayGetter +  1;
        this.thisDynArray[typeof(this.values)] * this.lenOfArray;
        this.thisDynArray = new Array(this.lenOfArray);
    }

    insertFrontArray =(val) => {
        
        // var copyArray = this.thisDynArray.fill()
        // var copyArray = this.thisDynArray.splice(0, this.thisDynArray.length - 1)
        var copyArray = this.thisDynArray.toSpliced(0, -1);
        // var copyArray = this.thisDynArray.map(() => this.thisDynArray.shift());
        // var copyArray2 = this.thisDynArray.forEach(this.thisDynArray.shift());
        this.resizeArray();

        // for (var i = 0; i <= copyArray.length; i++) {
        //     if (i == 0) {
        //         this.thisDynArray[i] = val;
        //     }
        //     else {
        //         this.thisDynArray[i] = copyArray[i-1];
        //     }
        // }
        
        var test3 = copyArray.filter(value => value);
        this.thisDynArray[0] = val;
        this.thisDynArray.fill(copyArray.unshift(), 1, this.lenOfArray);

        this.thisDynArray.flatMap((v) => new Array(self.lenOfArray).fill(v, 0, self.lenOfArray))

    }

    hashArray = () => {
        return this.dynArray.map(([length, value]) => (new Array(length)).fill(value, 0, length)).flat();
    }

    insertBackArray(val) {
        this.resizeArray();
        this.dynArray[this.len+1] = val;
      
        this.dynArray.map((value, index) => {if(index == len-1) {val}});

    }

    insertAtIndex(val, idx) {
        copyArray = this.dynArray.fill(value)
        for (var i = 0; i <= self.len; i++) {
            if (i != idx) {
                this.dynArray[i] = copyArray[i];
            }
            else {
                this.dynArray[idx] = val;
            }
        }
    }

    // sizeOfArray = (function () {
    //         this.sizeOfArray;
    // })();

    get sizeOfArrayGetter() {try {return this.thisDynArray.length;} catch(err) {return 0}}

    get indexGetter() {
        return this.dynArray.indexOf(val);
    }

    get currentLength() {
        return this.len;
    }

    clearArray = () => {
        this.dynArray.every(value, index => this.dynArray[index] = null);
    }

    // isEmpty = new function() {
    //     return this.len != 0;
    // }

    toString = () => {
        this.dynArray = this.dynArray.every(value => String(value) )
    }
}



dynamicArray = new DynamicArray([4,4,6,7]);

dynamicArray.createArray();
dynamicArray.insertFrontArray(5);
// dynamicArray.insertBackArray(5);
// dynamicArray.insertAtIndex(5, 3);
// dynamicArray.sizeOfArray();
// dynamicArray.isEmpty();
// dynamicArray.toString();
// dynamicArray.clearArray();
