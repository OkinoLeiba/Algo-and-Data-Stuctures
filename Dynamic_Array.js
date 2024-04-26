class DynamicArray {
    constructor(values, dynArray, sizeOfArray) {
        this.values = values | null;
        this.dynArray = [typeof(this.values)];
        this.sizeOfArray = 0;
        this.len = dynArray.length;
    }

    // dynArray1 = new Array(5);
    // dynArray1.apply(this, Array(5)).map(() => {})

    createArray() {
        this.dynArray.fill((value = 0) => {value += 1; this.sizeOfArray += 1;});
    }

    resizeArray() {
        this.sizeOfArray += 1;
        this.dynArray[typeof(this.values)] * this.sizeOfArray;
        this.dynArray = new Array(this.sizeOfArray);
    }

    insertFrontArray = (val) => {
        copyArray = this.dynArray.fill(value)
        this.resizeArray();

        for (var i = 0; i <= this.len; i++) {
            if (i == 0) {
                this.dynArray[i] = val;
            }
            else {
                this.dynArray[i] = copyArray[i-1];
            }
        }

        this.dynArray[0] = val;
        this.dynArray.fill(value, 1, length);

        this.dynArray.flatMap((v) => new Array(self.len).fill(v, 0, self.len))

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

    sizeOfArray = (function () {
            return this.sizeOfArray;
    })();

    get indexGetter() {
        return this.dynArray.indexOf(val);
    }

    get currentLength() {
        return this.len;
    }

    clearArray = () => {
        this.dynArray.every(value, index => this.dynArray[index] = null);
    }

    isEmpty = new function() {
        return this.len != 0;
    }

    toString = () => {
        this.dynArray = this.dynArray.every(value => String(value) )
    }
}



dynamicArray = new DynamicArray();

dynamicArray.createArray();
dynamicArray.insertFrontArray(5);
dynamicArray.insertBackArray(5);
dynamicArray.insertAtIndex(5, 3);
dynamicArray.sizeOfArray();
dynamicArray.isEmpty();
dynamicArray.toString();
dynamicArray.clearArray();
