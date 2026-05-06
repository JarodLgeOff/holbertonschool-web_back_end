function createInt8TypedArray(length, position, value) {
    const len = Number(length);
    const pos = Number(position);
    const val = Number(value);

    if (!Number.isInteger(len) || len < 0) {
        throw new Error('Position outside range');
    }
    if (!Number.isInteger(pos) || pos < 0 || pos >= len) {
        throw new Error('Position outside range');
    }

    const buffer = new ArrayBuffer(len);
    const view = new Int8Array(buffer);
    view[pos] = val;
    return new DataView(buffer);
}

export default createInt8TypedArray;